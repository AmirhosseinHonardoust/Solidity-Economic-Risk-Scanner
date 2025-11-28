from typing import List
from se_risk_scanner.models import ContractProfile, RiskFinding
from se_risk_scanner.features.invariants import analyze_invariants


def missing_safety_bounds_rule(profile: ContractProfile) -> List[RiskFinding]:
    """If LTV/collateral ratio appears without clear bounds, flag design risk."""
    features = analyze_invariants(profile)
    findings: List[RiskFinding] = []
    if features["mentions_ltv"] or features["mentions_collateral_ratio"]:
        findings.append(
            RiskFinding(
                contract=profile.name,
                category="INVARIANT",
                severity="LOW",
                code_reference=None,
                message="Potential missing safety bounds for LTV/collateral ratio",
                rationale="Contract references LTV or collateral ratios. Ensure explicit "
                          "bounds and checks exist to enforce safe ranges.",
            )
        )
    return findings
