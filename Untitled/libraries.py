import random

number = random.randint(1, 10)   # inclusive of range endpoints
print(number)

cards = ["jack", "queen", "king"]   # defining list in this order
random.shuffle(cards)   # takes list of values and shuffles them
for card in cards:  # for each of the cards in the loop
    print(card) # print it out one line at a time


# from random import choice   # shorter/tighter choice depending

# coin = choice(["heads", "tails"])


# import random # importing all of the content/functions in random

# coin = random.choice(["heads", "tails"])   # will provide a random selections from the list defined including "heads" and "tails"
# print(coin)