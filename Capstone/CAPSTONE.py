"""
Capstone Project
transformers quiz 
"""

import json
from pathlib import Path

input_file = Path(__file__).with_name("data.json")

with input_file.open("r", encoding="utf-8") as file:
    questions = json.load(file)


def run_quiz(questions):
    score = 0 
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for letter, choice in zip("ABCD", q["choices"]):
            print(f"{letter}. {choice}")

        user_letter = input("Your answer (A/B/C/D): ").strip().upper()
        mapping = dict(zip("ABCD", q["choices"]))
        user_choice = mapping.get(user_letter)
        
        if user_choice == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
        print()
    
    print(f"Your final score is {score}/{len(questions)}")
    
    print("\nWould you like to play again? (yes/no)")
    play_again = input().strip().lower()
    if play_again in ("yes", "y", "YES", "Yes", "Y", "ye", "Ye", "YE"):
        run_quiz(questions)
    elif play_again in ("no", "n", "NO", "No", "N"):
        print("Thanks for playing!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        run_quiz(questions)

if __name__ == "__main__":
    run_quiz(questions)
