import json
from typing import List, Tuple

from .models import ContractProfile, RiskFinding


def print_text_report(results: List[Tuple[ContractProfile, List[RiskFinding], dict]]) -> None:
    """Print a human-readable CLI report."""
    for profile, findings, score in results:
        print(f"Contract: {profile.name}")
        print(f"Overall Economic Risk Level: {score['level']} (score={score['score']})")
        if not findings:
            print("  No findings.\n")
            continue
        for f in findings:
            print(f"  [{f.severity}][{f.category}] {f.message}")
            if f.rationale:
                print(f"    -> {f.rationale}")
        print()


def to_json_report(results: List[Tuple[ContractProfile, List[RiskFinding], dict]]) -> str:
    """Return a JSON string containing all results."""
    output = []
    for profile, findings, score in results:
        output.append(
            {
                "contract": profile.name,
                "score": score,
                "findings": [f.to_dict() for f in findings],
            }
        )
    return json.dumps(output, indent=2)
