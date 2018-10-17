# this program is to create a guessing game where the user must guess the computers number.

import random


def random_number():
    """
    this program gets the random number
    :return: this returns the function
    """
    number = random.randint(1, 1000000000)
    return number


def answer():
    """
    this gets the users guess
    :return: this returns the function
    """
    user_answer = input("guess a number between 1 and 100")
    return float(user_answer)


def main():
    number = random_number()
    total_guess = 0
    while True:
        play = input("would you like to guess my number?(y/n)")
        if play == "n":
            print("fine then, i hope you have a less than good day")
            return False
        elif play == "y":
            break
        else:
            pass
    while True:
        guess = int(input("guess a number between 1 and 100"))
        total_guess += 1
        if guess == number:
            print("congratulations, you got my number, in only", total_guess, "guesses")
            print("hope to play with you again")
            break
        elif number < guess:
            print("your guess is too high")
        else:
            print("your guess is too low")


main()
