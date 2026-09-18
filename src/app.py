"""JSONL admission interface for the healthcare workload guard."""
import json
import sys
from src.workload_guard import Workload, admit


def evaluate(payload: dict) -> dict:
    admitted, blockers = admit(Workload(**payload))
    return {"input": payload, "admitted": admitted, "blockers": blockers}


for line in sys.stdin:
    if line.strip():
        print(json.dumps(evaluate(json.loads(line))))
