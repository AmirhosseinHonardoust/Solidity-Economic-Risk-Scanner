from typing import List
from se_risk_scanner.models import ContractProfile, RiskFinding

from .control_rules import centralized_control_rule
from .fee_rules import fee_complexity_rule
from .supply_rules import unbounded_mint_rule
from .liquidity_rules import blacklist_mechanism_rule
from .oracle_rules import manual_price_rule
from .invariant_rules import missing_safety_bounds_rule


RULES = [
    centralized_control_rule,
    fee_complexity_rule,
    unbounded_mint_rule,
    blacklist_mechanism_rule,
    manual_price_rule,
    missing_safety_bounds_rule,
]


def run_all_rules(profile: ContractProfile) -> List[RiskFinding]:
    """Run all economic rules on a contract profile."""
    findings: List[RiskFinding] = []
    for rule in RULES:
        try:
            findings.extend(rule(profile))
        except Exception as exc:
            findings.append(
                RiskFinding(
                    contract=profile.name,
                    category="ENGINE",
                    severity="LOW",
                    code_reference=None,
                    message=f"Rule {rule.__name__} raised an exception",
                    rationale=str(exc),
                )
            )
    return findings
