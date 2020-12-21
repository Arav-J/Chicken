# There are 4 Elements of {G, R, B, Y}
import random


def decide_the_code():
    Character_List: list = ["G", "R", "B", "Y"]

    final_code = [random.choice(Character_List) for i in range(4)]

    print(final_code)


def ask_guess():
    guess = [input("Input your guess.\n ->") for i in range(4)]

