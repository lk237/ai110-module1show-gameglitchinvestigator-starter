# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Game Glitch Investigator is a Streamlit number-guessing game. The app picks a secret number within a range that depends on the chosen difficulty (Easy: 1–20, Normal: 1–100, Hard: 1–50), and the player tries to guess it within a limited number of attempts. After each guess, the game gives a hint ("Go HIGHER" / "Go LOWER"), tracks a score, and ends with a win or a "game over" once attempts run out. The starter code was intentionally buggy — the goal of the assignment is to investigate and fix the glitches so the game plays correctly.
- The bugs I found are the following:
1. Backwards hints — Guessing 1 told you to "Go LOWER" and guessing 100 told you to "Go HIGHER." A glitch also converted the secret to a string on even attempts, breaking the numeric comparison.
2. "New Game" didn't reset — After losing, clicking "New Game" left the old status (and score/history) in st.session_state, so the board stayed stuck on the "Game over" screen until the page was refreshed.
3. Wrong range shown/used — The range prompt was hardcoded to "between 1 and 100," which was incorrect for Easy and Hard, and a new game's secret was generated with random.randint(1, 100) regardless of difficulty.
- The fixes I applied are the following:
1. Hints: Removed the even-turn string conversion so the secret is always an int, and mapped the correct outcome to each message (Too High → 📉 Go LOWER!, Too Low → 📈 Go HIGHER!) via OUTCOME_MESSAGES.
2. New Game: The reset block now fully clears state — secret, attempts, score, status (back to "playing"), and history — so a new game starts cleanly without a refresh.
3. Range: The prompt and the new-game secret both use get_range_for_difficulty(difficulty) (low/high) instead of hardcoded 1–100, and the game logic was refactored into logic_utils.py so it can be unit-tested (7 pytest tests pass).


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step --> User enters a guess of 50
2. <!-- Describe this step --> Game returns "Go higher"
3. <!-- Describe this step --> User enters a guess of 68 ->  Game returns "Go lower"
4. <!-- Describe this step --> User enters a guess of 63
5. <!-- Add more steps as needed --> Game returns "Correct" -> You won! The secret was 63. Final score: 35

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->
<img width="1332" height="622" alt="image" src="https://github.com/user-attachments/assets/ae97f37a-5f03-4521-ac21-d1634c6c08ef" />

## 🧪 Test Results

```
# $ pytest tests/
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
collected 7 items

tests\test_game_logic.py .......                                         [100%]

============================== 7 passed in 0.03s ==============================

```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
