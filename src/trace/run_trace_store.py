import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from langchain_core.documents import Document


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_localappdata() -> str:
    return os.environ.get("LOCALAPPDATA", ".")


def _trace_base_dir() -> Path:
    configured = os.getenv("METIS_TRACE_DIR")
    if configured:
        return Path(configured)
    return Path(_safe_localappdata()) / "Metis" / "traces"


def _trace_file_for_date(day: Optional[str] = None) -> Path:
    date_key = day or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return _trace_base_dir() / "runs" / f"{date_key}.jsonl"


def _document_to_dict(document: Document) -> Dict[str, Any]:
    metadata = dict(document.metadata) if document.metadata else {}
    return {
        "page_content": document.page_content,
        "metadata": metadata,
    }


def _normalize_documents(documents: List[Any]) -> List[Dict[str, Any]]:
    normalized: List[Dict[str, Any]] = []
    for item in documents or []:
        score = None
        document = item
        if isinstance(item, tuple) and len(item) == 2:
            document, score = item
        if not isinstance(document, Document):
            continue
        doc_payload = _document_to_dict(document)
        if score is not None:
            try:
                doc_payload["score"] = float(score)
            except (TypeError, ValueError):
                doc_payload["score"] = score
        normalized.append(doc_payload)
    return normalized


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


@dataclass
class RunTraceFilters:
    user_id: Optional[int] = None
    thread_id: Optional[str] = None
    knowledgebase_id: Optional[int] = None
    rag_type: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class RunTraceStore:
    def __init__(self) -> None:
        self.base_dir = _trace_base_dir()

    def append_run_trace(self, payload: Dict[str, Any]) -> Path:
        record = dict(payload)
        record.setdefault("timestamp", _utc_now_iso())
        record["retrieval"] = _normalize_documents(record.get("retrieval", []))
        if "documents" in record:
            record.pop("documents", None)
        record.setdefault("agent_events", [])
        record.setdefault("feedback", None)

        output_path = _trace_file_for_date()
        _ensure_parent(output_path)
        with output_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        return output_path

    def _iter_trace_files(self) -> List[Path]:
        runs_dir = self.base_dir / "runs"
        if not runs_dir.exists():
            return []
        return sorted(runs_dir.glob("*.jsonl"), reverse=True)

    def list_trace_files(self) -> List[Dict[str, Any]]:
        files: List[Dict[str, Any]] = []
        for path in self._iter_trace_files():
            try:
                stat = path.stat()
                files.append(
                    {
                        "name": path.name,
                        "path": str(path),
                        "size": stat.st_size,
                        "modified_at": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
                    }
                )
            except OSError:
                continue
        return files

    def _iter_records(self) -> List[Dict[str, Any]]:
        records: List[Dict[str, Any]] = []
        for trace_file in self._iter_trace_files():
            with trace_file.open("r", encoding="utf-8") as handle:
                for line in handle:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        records.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        records.sort(key=lambda item: item.get("timestamp", ""), reverse=True)
        return records

    def _matches_filters(self, record: Dict[str, Any], filters: RunTraceFilters) -> bool:
        if filters.user_id is not None and record.get("user_id") != filters.user_id:
            return False
        if filters.thread_id is not None and record.get("thread_id") != filters.thread_id:
            return False
        if filters.knowledgebase_id is not None and record.get("knowledgebase_id") != filters.knowledgebase_id:
            return False
        if filters.rag_type is not None and record.get("rag_type") != filters.rag_type:
            return False
        timestamp = record.get("timestamp", "")
        if filters.start_date and timestamp and timestamp < filters.start_date:
            return False
        if filters.end_date and timestamp and timestamp > filters.end_date:
            return False
        return True

    def list_runs(self, page: int = 1, page_size: int = 25, filters: Optional[RunTraceFilters] = None) -> Dict[str, Any]:
        filters = filters or RunTraceFilters()
        records = [r for r in self._iter_records() if self._matches_filters(r, filters)]
        total = len(records)
        start = max((page - 1) * page_size, 0)
        end = start + page_size
        items = records[start:end]

        def summarize(record: Dict[str, Any]) -> Dict[str, Any]:
            retrieval = record.get("retrieval", [])
            return {
                "run_id": record.get("run_id"),
                "timestamp": record.get("timestamp"),
                "user_id": record.get("user_id"),
                "thread_id": record.get("thread_id"),
                "knowledgebase_id": record.get("knowledgebase_id"),
                "rag_type": record.get("rag_type"),
                "query": record.get("query"),
                "retrieval_count": len(retrieval) if isinstance(retrieval, list) else 0,
                "has_feedback": bool(record.get("feedback")),
            }

        return {
            "items": [summarize(item) for item in items],
            "total": total,
            "page": page,
            "page_size": page_size,
        }

    def get_run(self, run_id: str) -> Optional[Dict[str, Any]]:
        for record in self._iter_records():
            if record.get("run_id") == run_id:
                return record
        return None

    def update_feedback(self, run_id: str, feedback: Any) -> bool:
        files = self._iter_trace_files()
        for file_path in files:
            changed = False
            updated_lines: List[str] = []
            with file_path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    payload = line.strip()
                    if not payload:
                        continue
                    try:
                        record = json.loads(payload)
                    except json.JSONDecodeError:
                        updated_lines.append(line)
                        continue
                    if record.get("run_id") == run_id:
                        record["feedback"] = feedback
                        changed = True
                        updated_lines.append(json.dumps(record, ensure_ascii=False) + "\n")
                    else:
                        updated_lines.append(json.dumps(record, ensure_ascii=False) + "\n")
            if changed:
                with file_path.open("w", encoding="utf-8") as handle:
                    handle.writelines(updated_lines)
                return True
        return False

    def delete_run(self, run_id: str) -> bool:
        files = self._iter_trace_files()
        for file_path in files:
            changed = False
            kept_lines: List[str] = []
            with file_path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    payload = line.strip()
                    if not payload:
                        continue
                    try:
                        record = json.loads(payload)
                    except json.JSONDecodeError:
                        kept_lines.append(line)
                        continue
                    if record.get("run_id") == run_id:
                        changed = True
                        continue
                    kept_lines.append(json.dumps(record, ensure_ascii=False) + "\n")
            if changed:
                with file_path.open("w", encoding="utf-8") as handle:
                    handle.writelines(kept_lines)
                return True
        return False

