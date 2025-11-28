from typing import List
from se_risk_scanner.models import ContractProfile, RiskFinding


def centralized_control_rule(profile: ContractProfile) -> List[RiskFinding]:
    """Naive rule: many onlyOwner uses => centralized control risk."""
    src = profile.raw_source
    count = src.count("onlyOwner")
    findings: List[RiskFinding] = []
    if count >= 3:
        findings.append(
            RiskFinding(
                contract=profile.name,
                category="CONTROL",
                severity="MEDIUM",
                code_reference=None,
                message="Heavy reliance on onlyOwner modifiers",
                rationale="Multiple onlyOwner usages suggest strongly centralized control. "
                          "Review whether owner privileges are appropriate.",
            )
        )
    return findings
