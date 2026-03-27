import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
from dotenv import load_dotenv
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


# Ensure RAGAS env vars are available even when backend is started via uvicorn directly.
load_dotenv()


def _safe_localappdata() -> str:
    return os.environ.get("LOCALAPPDATA", ".")


def get_eval_output_dir() -> Path:
    configured = os.getenv("METIS_EVAL_DIR")
    if configured:
        return Path(configured)
    return Path(_safe_localappdata()) / "Metis" / "evals"


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def _extract_contexts(trace: Dict[str, Any]) -> List[str]:
    contexts: List[str] = []
    for item in trace.get("retrieval", []) or []:
        if not isinstance(item, dict):
            continue
        content = item.get("page_content")
        if content:
            contexts.append(content)
    return contexts


def _to_ragas_samples(traces: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    samples: List[Dict[str, Any]] = []
    for trace in traces:
        sample = {
            "run_id": trace.get("run_id"),
            "question": trace.get("refined_query") or trace.get("query") or "",
            "answer": trace.get("final_answer") or "",
            "contexts": _extract_contexts(trace),
        }
        if trace.get("ground_truth"):
            sample["ground_truth"] = trace["ground_truth"]
        samples.append(sample)
    return samples


def _sanitize_for_json(value: Any) -> Any:
    """
    Convert non-JSON-safe float values (NaN/Inf) to None recursively.
    """
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return None
        return value
    if isinstance(value, dict):
        return {k: _sanitize_for_json(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize_for_json(v) for v in value]
    return value


def _clean_env(name: str, fallback: str | None = None) -> str | None:
    value = os.getenv(name, fallback)
    if value is None:
        return None
    # Protect against accidental spaces/quotes in .env values.
    cleaned = value.strip().strip('"').strip("'").strip()
    return cleaned or None


def _build_ragas_llm():
    """
    Build a judge LLM for RAGAS using OpenAI-compatible settings.
    """
    model_name = _clean_env("RAGAS_LLM_MODEL", "gpt-4o-mini")
    model_provider = _clean_env("RAGAS_MODEL_PROVIDER", "openai")
    # Prefer RAGAS-specific keys; fallback keeps backward compatibility.
    api_key = _clean_env("RAGAS_OPENAI_API_KEY") or _clean_env("OPENAI_API_KEY")
    base_url = _clean_env("RAGAS_OPENAI_BASE_URL") or _clean_env("OPENAI_BASE_URL")
    if not api_key:
        raise RuntimeError("RAGAS_OPENAI_API_KEY is required for RAGAS evaluation.")
    try:
        # Align with src/agent/api_llm.py initialization strategy.
        from langchain.chat_models import init_chat_model

        llm = init_chat_model(
            model_provider=model_provider,
            model=model_name,
            api_key=api_key,
            base_url=base_url,
            temperature=0,
        )
    except Exception:
        # Fallback for environments where init_chat_model path is unavailable.
        from langchain_openai import ChatOpenAI

        llm_kwargs: Dict[str, Any] = {
            "model": model_name,
            "openai_api_key": api_key,
            "api_key": api_key,
            "temperature": 0,
        }
        if base_url:
            llm_kwargs["openai_api_base"] = base_url
            llm_kwargs["base_url"] = base_url
        llm = ChatOpenAI(**llm_kwargs)
    return llm, model_name, model_provider, base_url, len(api_key)


def _build_ragas_embeddings():
    """
    Build embeddings for RAGAS metrics that require semantic similarity.
    """
    embed_provider = _clean_env("RAGAS_EMBED_PROVIDER", "openai").lower()

    if embed_provider == "ollama":
        from langchain_ollama.embeddings import OllamaEmbeddings

        embedding_model = _clean_env("RAGAS_EMBEDDING_MODEL", _clean_env("EMBED_MODEL", "nomic-embed-text:latest"))
        base_url = _clean_env("RAGAS_OLLAMA_BASE_URL") or _clean_env("LLM_BASE_URL", "http://localhost:11434")
        return OllamaEmbeddings(model=embedding_model, base_url=base_url), embedding_model

    from langchain_openai import OpenAIEmbeddings

    api_key = _clean_env("RAGAS_OPENAI_API_KEY") or _clean_env("OPENAI_API_KEY")
    base_url = _clean_env("RAGAS_OPENAI_BASE_URL") or _clean_env("OPENAI_BASE_URL")
    if not api_key:
        raise RuntimeError("RAGAS_OPENAI_API_KEY is required for OpenAI embeddings in RAGAS evaluation.")

    embedding_model = _clean_env("RAGAS_EMBEDDING_MODEL", "text-embedding-3-small")
    kwargs: Dict[str, Any] = {"model": embedding_model, "api_key": api_key}
    if base_url:
        kwargs["base_url"] = base_url
    try:
        return OpenAIEmbeddings(**kwargs), embedding_model
    except Exception:
        legacy_kwargs: Dict[str, Any] = {"model": embedding_model, "openai_api_key": api_key}
        if base_url:
            legacy_kwargs["openai_api_base"] = base_url
        return OpenAIEmbeddings(**legacy_kwargs), embedding_model


def evaluate_traces_file(trace_jsonl_path: str) -> Dict[str, Any]:
    """
    Evaluate traces from a JSONL file and write a local report artifact.
    """
    trace_path = Path(trace_jsonl_path)
    traces = _load_jsonl(trace_path)
    samples = _to_ragas_samples(traces)
    if not samples:
        raise ValueError("No valid trace samples found for evaluation.")

    try:
        from datasets import Dataset
        from ragas import evaluate
        from ragas.metrics import answer_relevancy, faithfulness
    except ImportError as exc:
        raise RuntimeError("RAGAS dependencies are not installed. Install requirements first.") from exc

    dataset_payload: Dict[str, List[Any]] = {
        "question": [s["question"] for s in samples],
        "answer": [s["answer"] for s in samples],
        "contexts": [s["contexts"] for s in samples],
    }
    has_ground_truth = any("ground_truth" in s for s in samples)
    if has_ground_truth:
        dataset_payload["ground_truth"] = [s.get("ground_truth", "") for s in samples]

    dataset = Dataset.from_dict(dataset_payload)
    metrics = [faithfulness, answer_relevancy]
    status = "ok"
    eval_error = None
    per_sample: List[Dict[str, Any]] = []
    aggregate: Dict[str, Any] = {}
    llm_model = None
    llm_provider = None
    llm_base_url = None
    embedding_model = None
    try:
        judge_llm, llm_model, llm_provider, llm_base_url, llm_key_length = _build_ragas_llm()
        judge_embeddings, embedding_model = _build_ragas_embeddings()

        result = evaluate(
            dataset=dataset,
            metrics=metrics,
            llm=judge_llm,
            embeddings=judge_embeddings,
        )
        frame = result.to_pandas()
        rows = frame.to_dict(orient="records")
        for index, rec in enumerate(rows):
            sample = samples[index]
            contexts = sample.get("contexts", []) or []
            context_chars = sum(len(c) for c in contexts if isinstance(c, str))
            faithfulness_value = rec.get("faithfulness")
            answer_relevancy_value = rec.get("answer_relevancy")
            per_sample.append({
                "run_id": sample.get("run_id"),
                "question": sample.get("question"),
                "diagnostics": {
                    "context_count": len(contexts),
                    "context_total_chars": context_chars,
                    "answer_chars": len(sample.get("answer", "")),
                    "faithfulness_missing": faithfulness_value is None,
                    "answer_relevancy_missing": answer_relevancy_value is None,
                },
                **rec,
            })
        for key in frame.columns:
            try:
                aggregate[key] = float(frame[key].mean())
            except Exception:
                continue
    except Exception as exc:
        status = "failed"
        eval_error = str(exc)

    eval_id = f"eval-{_utc_timestamp()}"
    output_dir = get_eval_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{eval_id}.json"
    payload = {
        "eval_id": eval_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_file": str(trace_path),
        "sample_count": len(samples),
        "status": status,
        "error": eval_error,
        "llm_model": llm_model,
        "embedding_model": embedding_model,
        "runtime_config": {
            "llm_provider": llm_provider,
            "llm_base_url": llm_base_url,
            "llm_key_length": llm_key_length if 'llm_key_length' in locals() else None,
        },
        "diagnostics": {
            "total_samples": len(samples),
            "faithfulness_missing_samples": sum(
                1 for item in per_sample if item.get("diagnostics", {}).get("faithfulness_missing")
            ),
            "answer_relevancy_missing_samples": sum(
                1 for item in per_sample if item.get("diagnostics", {}).get("answer_relevancy_missing")
            ),
        },
        "metrics": aggregate,
        "samples": per_sample,
    }
    payload = _sanitize_for_json(payload)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    return payload


def list_evaluations(page: int = 1, page_size: int = 25) -> Dict[str, Any]:
    output_dir = get_eval_output_dir()
    if not output_dir.exists():
        return {"items": [], "total": 0, "page": page, "page_size": page_size}

    files = sorted(output_dir.glob("eval-*.json"), reverse=True)
    total = len(files)
    start = max((page - 1) * page_size, 0)
    end = start + page_size
    items: List[Dict[str, Any]] = []
    for path in files[start:end]:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        payload = _sanitize_for_json(payload)
        items.append(
            {
                "eval_id": payload.get("eval_id"),
                "created_at": payload.get("created_at"),
                "sample_count": payload.get("sample_count", 0),
                "metrics": payload.get("metrics", {}),
                "source_file": payload.get("source_file"),
            }
        )
    return {"items": items, "total": total, "page": page, "page_size": page_size}


def get_evaluation(eval_id: str) -> Dict[str, Any]:
    path = get_eval_output_dir() / f"{eval_id}.json"
    if not path.exists():
        raise FileNotFoundError(f"Evaluation not found: {eval_id}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    return _sanitize_for_json(payload)


def delete_evaluation(eval_id: str) -> bool:
    path = get_eval_output_dir() / f"{eval_id}.json"
    if not path.exists():
        return False
    path.unlink()
    return True

