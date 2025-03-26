#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program checks if the user guesses the random number correctly
import random


def main():
    # generate random number
    random_number = random.randint(1, 9)

    # get user's guess
    user_guess = int(input("Enter your guess: "))
    print("")

    # check if the user's guess is correct
    if user_guess == random_number:
        print("You guessed the correct number!")
    else:
        print("You guessed the wrong number. The correct number was", random_number)

        main()

        # Run the program


if __name__ == "__main__":
    main()
