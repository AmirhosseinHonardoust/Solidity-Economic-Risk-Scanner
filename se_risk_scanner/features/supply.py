from .typing import Profile


def analyze_supply(profile: Profile) -> dict:
    """Analyze supply-related aspects: mint, burn, caps, maxSupply."""
    low = profile.raw_source.lower()
    return {
        "has_mint": "mint(" in low,
        "has_burn": "burn(" in low,
        "mentions_max_supply": "maxsupply" in low.replace("_", ""),
    }
