import random
num = random.randint(1, 20)

message = """\nWelcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have a number of chances to guess the correct number."""

level = """
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n"""

LEVELS = {
    "1": "Easy",
    "2": "Medium",
    "3": "Hard"
}

CHANCES = {
    "Easy": 10,
    "Medium": 5,
    "Hard": 3
}


print(message)


def main():
    print(level)
    try:
        # Get user input for difficulty level
        while True:
            difficulty = input("Enter your choice: ")
            if not difficulty.isdigit():
                print("Please enter a number [1, 2, 3]\n")
            else:
                print(
                    f"\nGreat! You have selected the {LEVELS[difficulty]} difficulty level.\nLet's start the game!\n")
                break

        # Ask the player to guess.
        for guessesTaken in range(1, (CHANCES[LEVELS[difficulty]] + 1)):
            guess = input("Enter your guess: ")

            if not guess.isdigit():
                print(f"Incorrect! The number should be an integer.\n")
                guess = 0
            elif int(guess) < num:
                print(f"Incorrect! The number is greater than {guess}.\n")
            elif int(guess) > num:
                print(f"Incorrect! The number is less than {guess}.\n")
            else:
                break  # meaning this guess is the correct answer

        if guess == num:
            print(
                f"Congratulations! You guessed the correct number in {guessesTaken} attempts.\n")
            answer = input("Would you like to play again? (Y/n): ")
        else:
            print(f"You ran out of guesses. I was thinking of {num}.\n")
            answer = input("Would you like to play again? (Y/n): ")

        if answer.lower() == "y":
            main()
        else:
            print("Thank you for playing my game! :) \n")

    # If user presses ctrl+c
    except KeyboardInterrupt:
        print("\nThank you for playing my game! :) \n")


if __name__ == "__main__":
    main()
