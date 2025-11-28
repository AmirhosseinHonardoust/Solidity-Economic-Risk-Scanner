from .typing import Profile


def analyze_liquidity_features(profile: Profile) -> dict:
    """Scan for liquidity/trading hints: anti-bot, cooldown, blacklist."""
    low = profile.raw_source.lower()
    return {
        "mentions_liquidity": "liquidity" in low,
        "mentions_blacklist": "blacklist" in low,
        "mentions_cooldown": "cooldown" in low,
        "mentions_antibot": "anti bot" in low or "antibot" in low,
    }
