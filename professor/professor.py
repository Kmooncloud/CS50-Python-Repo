# pset4 Little Professor 
# asks user to answer 10 simple math problems based on 1,2, or 3 digit level 
# allows for 3 attempts to answer and then outputs the correct answer and -1 point 
# prints out final score at the end 

import random
import sys


def main():
    level = get_level()
    level = int(level)

    rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    score = int()
    for _ in rounds:    # will repeat all the following code 10x
        print(f"Score: {score}")
        score += get_math(level)
    print(f"Score: {score}")


def get_math(level):    # return 1 for right return 0 for wrong
    a = generate_integer(level)
    b = generate_integer(level)
    ans = a + b
    print(f"Answer saved: {ans}")
    guess = get_guess(a, b)
    if guess == ans:
        return 1
    elif guess != ans:
        wrong = 1
        print("EEE")
        while wrong != 3:
            get_guess(a, b)
            if ans != guess:
                print("EEE")
                wrong += 1
            else:
                return 1
        print(f"{a} + {b} = {ans}")
        return 0
    else:
        sys.exit("Error missed in get_math")

def get_guess(a, b):
    while True:
        try:
            guess = input(f"{a} + {b} = ")
            guess = int(guess)
            return guess
        except ValueError:
            print("EEE @ get_guess")
            pass

def get_level():
    # propmpts user until 1, 2, or 3 has been input
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if 1 <= level <= 3:
                return level
            else:
                get_level()
        except (ValueError, TypeError):
            pass

def generate_integer(level):
    # returns a randomly generated int with (level) digits
    # raises a ValueError if (level) is not 1, 2 or 3
    n = int()
    if level < 1 or level > 3:
        raise ValueError
    elif level == 1:
        n = random.randint(0,9)
    elif level == 2:
        n = random.randint(10,99)
    elif level == 3:
        n = random.randint(100,999)
    else:
        sys.exit("error missed in generate_int")
    return n

if __name__ == "__main__":
    main()