# pset4 Guesing Game
# Prompt the user for a number, n, for the level of the game
# set n = random int between 1-n and ahve the user guess until correct

import random
import sys

def main(): # get a level >= 1 and handle special case when level == 1
    try:
        n = int(input("Level: "))
        if n < 1:
            main()
    except ValueError:
        main()

    ans = int()
    if n == 1:
        guess(1, 1)
    else:
        ans = random.randint(1, n)
        guess(ans, n)

    sys.exit("Just right!") # sys.exit to end program required by check50

def guess(ans, n):  # have user make positive whole number guesses until correct 
    try:
        inguess = int(input("Guess: "))
    except ValueError:
        guess(ans, n)

    if inguess == ans:
        return
    elif inguess > ans and inguess <= n:
        print("Too large!")
        guess(ans, n)
    elif inguess < ans and inguess >= 1:
        print("Too small!")
        guess(ans, n)
    elif inguess < 1 or inguess > n:
        guess(ans, n)

main()