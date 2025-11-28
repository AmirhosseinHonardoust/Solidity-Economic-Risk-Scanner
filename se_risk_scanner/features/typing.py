from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from se_risk_scanner.models import ContractProfile

# At runtime, Profile is just a forward-ref string.
# Type checkers will still understand it as ContractProfile.
Profile = "ContractProfile"
