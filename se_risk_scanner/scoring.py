from typing import Iterable, Dict
from se_risk_scanner.models import RiskFinding


SEVERITY_WEIGHTS: Dict[str, int] = {
    "LOW": 1,
    "MEDIUM": 3,
    "HIGH": 7,
    "CRITICAL": 10,
}


def score_contract(findings: Iterable[RiskFinding]) -> dict:
    """Aggregate findings into a simple numeric risk score."""
    total = 0
    counts: Dict[str, int] = {}
    for f in findings:
        w = SEVERITY_WEIGHTS.get(f.severity.upper(), 1)
        total += w
        counts[f.severity] = counts.get(f.severity, 0) + 1

    if total == 0:
        level = "NONE"
    elif total < 5:
        level = "LOW"
    elif total < 15:
        level = "MEDIUM"
    elif total < 30:
        level = "HIGH"
    else:
        level = "CRITICAL"

    return {"score": total, "level": level, "severity_counts": counts}
