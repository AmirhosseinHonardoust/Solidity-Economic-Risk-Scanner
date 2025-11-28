from .typing import Profile


def extract_roles(profile: Profile) -> dict:
    """Placeholder role extraction (e.g., onlyOwner)."""
    return {
        "raw_modifiers": profile.modifiers,
        "has_only_owner": "onlyOwner" in profile.raw_source,
    }
