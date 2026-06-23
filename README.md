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

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

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
