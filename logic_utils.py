def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # ORIGINAL STARTER (resolved):
    # FIXME: Logic missing here. The working version lives in app.py (lines 4-11).
    # Copy that implementation in so app.py can import it from this file instead.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # ORIGINAL STARTER (resolved):
    # FIXME: Logic missing here. The working version lives in app.py (lines 14-29).
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        # Accept "42" and "42.0" alike by routing decimals through float first.
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome as a string.

    Returns one of: "Win", "Too High", "Too Low"

    NOTE: This returns a plain STRING (not a tuple), so it matches
    tests/test_game_logic.py. The user-facing hint message is built in app.py.
    """
    # ORIGINAL STARTER (resolved):
    # FIXME: Logic missing here. The working version lives in app.py (lines 32-39).
    # WATCH OUT: app.py's check_guess returns a TUPLE -> ("Win", "🎉 Correct!"),
    # but tests/test_game_logic.py expects a plain STRING -> "Win".
    # The function and the tests must agree, or pytest will fail on a tuple-vs-string mismatch.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # ORIGINAL STARTER (resolved):
    # FIXME: Logic missing here. The working version lives in app.py (lines 42-57).
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
