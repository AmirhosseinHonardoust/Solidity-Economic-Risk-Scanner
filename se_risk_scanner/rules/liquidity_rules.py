from typing import List
from se_risk_scanner.models import ContractProfile, RiskFinding
from se_risk_scanner.features.liquidity import analyze_liquidity_features


def blacklist_mechanism_rule(profile: ContractProfile) -> List[RiskFinding]:
    """If blacklist logic is present, flag liquidity/user risk."""
    f = analyze_liquidity_features(profile)
    findings: List[RiskFinding] = []
    if f["mentions_blacklist"]:
        findings.append(
            RiskFinding(
                contract=profile.name,
                category="LIQUIDITY",
                severity="MEDIUM",
                code_reference=None,
                message="Blacklist functionality detected",
                rationale="Blacklist logic can be used to selectively trap user balances or "
                          "block sells. Carefully review owner privileges.",
            )
        )
    return findings
