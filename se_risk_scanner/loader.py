import os
from typing import Dict


def load_contract_sources(path: str) -> Dict[str, str]:
    """Load Solidity files from a file or directory.

    Returns a mapping: { name_or_path: source_code }.
    """
    sources: Dict[str, str] = {}

    if os.path.isfile(path) and path.endswith(".sol"):
        with open(path, "r", encoding="utf-8") as f:
            sources[os.path.basename(path)] = f.read()
        return sources

    if os.path.isdir(path):
        for root, _dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(".sol"):
                    full = os.path.join(root, filename)
                    with open(full, "r", encoding="utf-8") as f:
                        sources[full] = f.read()
    return sources
