from se_risk_scanner.loader import load_contract_sources


def test_load_contract_sources(tmp_path):
    f = tmp_path / "test.sol"
    f.write_text("// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;")
    sources = load_contract_sources(str(tmp_path))
    assert len(sources) == 1
