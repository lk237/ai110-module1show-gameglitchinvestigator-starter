# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? When the game pop up, it actually looks good. When you start playing that's when you realise there's a lot glitches. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards"). The 1st example I found is that when you lose the game and you click on new game, it doesn't reset. you have to refresh the whole page. The other examples are about the hint function. It  doesn't respect the boundaries for example we can only guess from 1 to 100 but when you put 1 the hint asks you to go lower. The same happen sometimes when you guess 100, the hints asks you to go higher. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess 1|"Go higher" hint   | "Go lower" hint |       None
|Guess 100|"Go lower" hint  | "Go higher" hint |  none
|Lose a game, then click "New Game" | Board resets (new secret, score 0, can play again) | Stayed stuck on the "Game over" screen; had to refresh the whole page | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). For the "New Game" bug, the AI pointed out that the button only reset `attempts` and `secret` but never reset `status` back to "playing" (so a lost game stayed stuck on the "Game over" screen until I refreshed). It suggested also resetting `status`, `score`, and `history` in the new-game block. I verified this by losing a game on purpose, clicking "New Game," and confirming the board reset without refreshing the page.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). For the backwards hints, the AI first told me the cause was a glitch that turned the secret into a string on even turns, and said removing that conversion would fix it. That explanation sounded convincing, but when I tested it the hints were still backwards. The real cause was that the hint messages in `check_guess` were simply swapped ("too high" returned "Go HIGHER!" instead of "Go LOWER!"). I caught it by guessing 1 and 100 again after the first "fix" and seeing the hint still point the wrong way, which taught me to test every fix instead of trusting the AI's first explanation.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I decided a bug was really fixed only after I reproduced the original broken behavior, applied the fix, and then could no longer trigger it. I didn't trust a fix just because the code "looked right" or because the AI said it was fixed. The hint bug taught me this the hard way: the first fix seemed reasonable but the hints were still backwards, so I learned that a fix isn't done until the actual symptom is gone.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I ran a manual boundary test in the running Streamlit app: I guessed 1 and expected "Go HIGHER," then guessed 100 and expected "Go LOWER," and repeated this across several turns. The first time, guess 1 still told me to "Go LOWER," which showed me the hint messages in `check_guess` were swapped rather than caused by the string conversion. After the real fix, guessing 1 always said "Go HIGHER" and 100 always said "Go LOWER" on every turn, which confirmed the comparison logic was finally correct.
- Did AI help you design or understand any tests? How? Yes.The AI suggested testing the edge values (1 and 100) specifically, because those boundaries are where a reversed or text-based comparison shows up most clearly. It also helped me understand why the broken version failed by walking through the comparison step by step (for example, why comparing a number to a string raised an error and fell back to comparing them as text). That made me realize a good test targets the exact boundary where the logic is most likely to break.


## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? I would tell them that every time you click a button or type something, Streamlit re-runs the whole script from top to bottom, like refreshing the page. Because of that, any normal variable gets wiped and reset on every interaction, so you can't just store the secret number or the score in a regular variable. That is what `st.session_state` is for: it's a little memory box that survives across reruns, so the secret, attempts, score, and history stay the same until you choose to change them. This project showed me that directly the "New Game" bug happened because the reset code only changed some of the session_state values and left the old `status` behind, so the game kept thinking it was over even after a rerun.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git. The habit I want to keep is writing a small automated test for every bug I fix, especially at the boundaries (like guessing 1 and 100). Once I had pytest tests for the reversed-hint bug, I could re-run them in a second and know the fix was still working instead of clicking through the app by hand every time. It turns "I think it's fixed" into "I can prove it's fixed," and it protects me from breaking the same thing again later.
- What is one thing you would do differently next time you work with AI on a coding task? Next time I would ask the AI to explain *why* a bug happens and show me the exact line before I let it suggest a fix, instead of accepting the first confident explanation. With the backwards-hint bug, the AI's first answer sounded right but was wrong, and I wasted time on it. Slowing down to verify the cause first would have saved me a step.
- In one or two sentences, describe how this project changed the way you think about AI generated code. I now treat AI-generated code as a fast first draft from a teammate who is often right but sometimes confidently wrong, not as a finished answer. My job is to read it, test it, and reproduce the bug myself before I trust that it's actually fixed.
