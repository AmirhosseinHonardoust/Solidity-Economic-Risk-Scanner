from .typing import Profile


def detect_fee_patterns(profile: Profile) -> dict:
    """Very naive fee pattern detection."""
    src = profile.raw_source
    low = src.lower()
    return {
        "mentions_fee": "fee" in low,
        "mentions_tax": "tax" in low,
        "mentions_transfer": "_transfer" in src,
    }
