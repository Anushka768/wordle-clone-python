# Wordle Clone 
A text-based Wordle-style game implemented in Python.

## Features
- Load words from a file
- Randomly select a target word
-  Evaluates each user guess and provides feedback using symbols:
  - `*` → Correct letter in correct position  
  - `?` → Correct letter, wrong position  
  - `_` → Letter not in the target word 
- Track letters used

## Concepts and Skills Demonstrated

| Concept | Description |
|----------|--------------|
| **File Handling** | Reads and validates words from a text file using `open()` and loops. |
| **Validation Logic** | Ensures that all words are alphabetic and of equal length. |
| **Randomization** | Uses the `random` module to pick a random target word. |
| **String Manipulation** | Compares guessed letters to the target word and builds feedback symbols. |
| **List Operations** | Maintains a list of available letters (True/False values). |
| **Conditional Logic** | Determines correctness and updates available letters. |
| **Functions & Modularity** | Organized into reusable functions for loading, choosing, updating, and scoring. |
| **User Interaction** | Takes console input for guesses and displays feedback dynamically. |

## How to run
1. Clone the repo
2. Ensure `targets.txt` and `legal.txt` are in the same folder
3. Run `test_wordle.py`:
```bash
python test_wordle.py
