from typing import List
from se_risk_scanner.models import ContractProfile, RiskFinding
from se_risk_scanner.features.oracle import analyze_oracle_usage


def manual_price_rule(profile: ContractProfile) -> List[RiskFinding]:
    """If manual price setters exist, flag arbitrary pricing risk."""
    features = analyze_oracle_usage(profile)
    findings: List[RiskFinding] = []
    if features["has_manual_price_setter"]:
        findings.append(
            RiskFinding(
                contract=profile.name,
                category="ORACLE",
                severity="HIGH",
                code_reference=None,
                message="Manual price setter detected",
                rationale="Functions like setPrice() or updatePrice() may allow privileged "
                          "accounts to arbitrarily change pricing, which can break lending, "
                          "AMM, or liquidation logic.",
            )
        )
    return findings
