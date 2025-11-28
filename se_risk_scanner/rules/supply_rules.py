from typing import List
from se_risk_scanner.models import ContractProfile, RiskFinding
from se_risk_scanner.features.supply import analyze_supply


def unbounded_mint_rule(profile: ContractProfile) -> List[RiskFinding]:
    """If mint() exists but max supply is not mentioned, flag risk."""
    features = analyze_supply(profile)
    findings: List[RiskFinding] = []
    if features["has_mint"] and not features["mentions_max_supply"]:
        findings.append(
            RiskFinding(
                contract=profile.name,
                category="SUPPLY",
                severity="HIGH",
                code_reference=None,
                message="Mint function without explicit max supply",
                rationale="Contract defines minting logic but does not reference an obvious "
                          "max supply or cap. This may allow unbounded inflation.",
            )
        )
    return findings
