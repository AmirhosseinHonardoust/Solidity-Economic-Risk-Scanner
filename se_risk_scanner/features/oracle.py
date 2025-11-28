from .typing import Profile


def analyze_oracle_usage(profile: Profile) -> dict:
    """Detect oracle/pricing patterns: Chainlink, Uniswap, manual price setters."""
    src = profile.raw_source
    low = src.lower()
    return {
        "uses_chainlink": "chainlink" in low or "aggregatorv3interface" in src,
        "uses_uniswap_price": "uniswap" in low and "price" in low,
        "has_manual_price_setter": "setprice" in low or "updateprice" in low,
    }
