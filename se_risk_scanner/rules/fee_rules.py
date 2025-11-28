from typing import List
from se_risk_scanner.models import ContractProfile, RiskFinding
from se_risk_scanner.features.fees import detect_fee_patterns


def fee_complexity_rule(profile: ContractProfile) -> List[RiskFinding]:
    """If both 'fee' and 'tax' appear, flag complex fee economics."""
    features = detect_fee_patterns(profile)
    findings: List[RiskFinding] = []
    if features["mentions_fee"] and features["mentions_tax"]:
        findings.append(
            RiskFinding(
                contract=profile.name,
                category="FEES",
                severity="MEDIUM",
                code_reference=None,
                message="Complex fee/tax logic detected",
                rationale="Contract mentions both fees and taxes. Complex transfer economics "
                          "may hide abusive tokenomics.",
            )
        )
    return findings
