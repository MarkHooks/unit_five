#this program is to create a guessing game where the user must guess the computers number.
import random


def random_number():
    number = random.randint(1, 100)
    print(number)
    return number


def answer():
    user_answer = input("guess a number between 1 and 100")
    return float(user_answer)


def main():
    number = random_number()
    while True:
        play = input("would you like to guess my number?(y/n)")
        if play == "n":
            pass
        elif play == "y":
            break
        else:
            return False
    while True:
        guess = int(input("guess a number between 1 and 100"))
        if guess == number:
            print("congratulations, you got my number, which was", number)
            break
        elif number < guess:
            print("your guess is too high")
        else:
            print("your guess is too low")


main()
