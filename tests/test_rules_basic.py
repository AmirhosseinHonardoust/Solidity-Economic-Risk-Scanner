from se_risk_scanner.models import ContractProfile
from se_risk_scanner.rules.runner import run_all_rules


def test_run_rules_on_empty_contract():
    profile = ContractProfile(
        name="Empty",
        inherits_from=[],
        functions=[],
        variables=[],
        events=[],
        modifiers=[],
        raw_source="",
    )
    findings = run_all_rules(profile)
    assert isinstance(findings, list)
