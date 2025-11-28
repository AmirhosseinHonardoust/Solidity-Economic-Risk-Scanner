from .typing import Profile


def analyze_invariants(profile: Profile) -> dict:
    """Look for AMM/lending invariants: constant product, LTV, collateral ratio."""
    low = profile.raw_source.lower()
    return {
        "mentions_constant_product": "x * y" in low or "xy" in low,
        "mentions_ltv": "ltv" in low or "loan-to-value" in low,
        "mentions_collateral_ratio": "collateral" in low and "ratio" in low,
    }
