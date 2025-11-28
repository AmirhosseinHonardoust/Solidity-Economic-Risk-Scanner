from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass
class FunctionInfo:
    name: str
    visibility: str
    modifiers: List[str]
    is_payable: bool
    writes_to: List[str]
    reads_from: List[str]
    raw_source: str


@dataclass
class VariableInfo:
    name: str
    var_type: str
    visibility: str
    is_constant: bool
    initial_value: Optional[str]


@dataclass
class ContractProfile:
    name: str
    inherits_from: List[str]
    functions: List[FunctionInfo]
    variables: List[VariableInfo]
    events: List[str]
    modifiers: List[str]
    raw_source: str


@dataclass
class RiskFinding:
    contract: str
    category: str
    severity: str  # e.g., "LOW", "MEDIUM", "HIGH", "CRITICAL"
    code_reference: Optional[str]
    message: str
    rationale: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "contract": self.contract,
            "category": self.category,
            "severity": self.severity,
            "code_reference": self.code_reference or "",
            "message": self.message,
            "rationale": self.rationale,
        }
