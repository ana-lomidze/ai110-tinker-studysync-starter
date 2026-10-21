"""
Target file for Tinker 1B, Part 2.

Move `apply_streak_bonus(combined_score, streak_days)` here from scoring.py,
then update the import at the top of scoring.py so `run_demo()` and the
Session Scorer tab still work exactly as before.
"""

# Moved from scoring.py so shared scoring logic lives in one place.
def apply_streak_bonus(combined_score: float, streak_days: int) -> float:
    """Add a bonus for consecutive study days, capped at 100."""
    if not 0 <= combined_score <= 100:
        raise ValueError(f"session score must be between 0 and 100, got {combined_score}")
    if streak_days < 0:
        raise ValueError(f"streak_days must be non-negative, got {streak_days}")
    boosted = combined_score + streak_days * 2
    return min(boosted, 100)
