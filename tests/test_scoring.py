from se_risk_scanner.models import RiskFinding
from se_risk_scanner.scoring import score_contract


def test_score_contract():
    findings = [
        RiskFinding("C", "SUPPLY", "HIGH", None, "msg", "rat"),
        RiskFinding("C", "FEES", "MEDIUM", None, "msg", "rat"),
    ]
    result = score_contract(findings)
    assert result["score"] > 0
    assert result["level"] in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
