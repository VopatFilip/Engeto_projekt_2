"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Vopát
email: vopat.f@gmail.com
discord: filipvopat
"""

import random


# Function to generate a random 4-digit number with unique digits
def generate_secret_number():
    while True:
        secret_number = str(random.randint(1000, 9999))
        if len(set(secret_number)) == 4 and secret_number[0] != '0':
            return secret_number


# Function to evaluate the user's guess
def evaluate_guess(secret_number, user_guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            bulls += 1
        elif user_guess[i] in secret_number:
            cows += 1
    return bulls, cows


# Determine rating based on the number of guesses
def get_rating(guesses):
    if guesses <= 10:
        return "amazing"
    elif guesses <= 15:
        return "good"
    elif guesses <= 20:
        return "average"
    else:
        return "not so good"


# Main game loop
def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()
    attempts = 0

    while True:
        user_input = input("Enter a 4-digit number: ")

        if not user_input.isdigit() or len(user_input) != 4 or len(set(user_input)) != 4 or user_input[0] == '0':
            print("Invalid input. Please enter a 4-digit number with unique digits and no leading zero.")
            continue

        attempts += 1

        bulls, cows = evaluate_guess(secret_number, user_input)

        if bulls == 4:
            rating = get_rating(attempts)
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print("-----------------------------------------------")
            print(f"That's {rating}!")
            break
        else:
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")
            print("-----------------------------------------------")


if __name__ == "__main__":
    main()
