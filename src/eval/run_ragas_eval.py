import argparse
import json

from src.eval.ragas_runner import evaluate_traces_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Run offline RAGAS evaluation from trace JSONL.")
    parser.add_argument("--trace-file", required=True, help="Path to a trace JSONL file.")
    args = parser.parse_args()

    result = evaluate_traces_file(args.trace_file)
    print(json.dumps(
        {
            "eval_id": result["eval_id"],
            "sample_count": result["sample_count"],
            "metrics": result["metrics"],
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()

