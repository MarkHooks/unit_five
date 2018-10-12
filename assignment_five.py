import random

def random_number():
    print(random.randint(1, 100))

def answer():

    user_answer = input("guess a number between 1 and 100")
    return float(user_answer)


def main():
    random_number1 = random_number()
    while True:
        answer(user_answer)
        if answer(user_answer) == random_number1:
            print("congratulations, you got the number")
            break
        else:
            pass




main()