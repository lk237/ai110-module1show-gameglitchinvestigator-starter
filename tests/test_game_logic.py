from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# NEW TEST: boundary check from the reflection log. Guessing the lowest value (1)
# when the secret is higher must say "Too Low" (so the app hints "Go HIGHER"),
# and guessing the highest value must say "Too High". This is exactly the bug
# that was reversed at the start, so it locks the fix in place.
def test_low_boundary_is_too_low():
    # Secret is 100, guess the floor (1) -> guess is below the secret
    assert check_guess(1, 100) == "Too Low"

def test_high_boundary_is_too_high():
    # Secret is 1, guess the ceiling (100) -> guess is above the secret
    assert check_guess(100, 1) == "Too High"

# NEW TEST: each difficulty maps to its own range. This guards the bug where the
# range was hardcoded to "1 to 100" regardless of difficulty.
def test_ranges_per_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)

# NEW TEST: parse_guess accepts whole numbers and rejects junk input.
def test_parse_guess_handles_valid_and_invalid():
    ok, value, err = parse_guess("42")
    assert ok and value == 42 and err is None

    bad_ok, bad_value, bad_err = parse_guess("abc")
    assert bad_ok is False and bad_value is None and bad_err
