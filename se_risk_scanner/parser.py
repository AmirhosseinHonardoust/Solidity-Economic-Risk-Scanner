from typing import Dict, List

from .models import ContractProfile


def parse_contracts(sources: Dict[str, str]) -> List[ContractProfile]:
    """Very naive placeholder parser.

    For now, this treats each source as a single ContractProfile with only raw source.
    Later you can integrate a real Solidity AST parser.
    """
    profiles: List[ContractProfile] = []
    for name, src in sources.items():
        profile = ContractProfile(
            name=name,
            inherits_from=[],
            functions=[],
            variables=[],
            events=[],
            modifiers=[],
            raw_source=src,
        )
        profiles.append(profile)
    return profiles
