# pset2 Nutrition Facts
# indexes through and returns the value from an input key in a dictionary 

fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelone": "80"
}

def main():
    item = input("Item: ")
    calories(item.lower())

def calories(item):
    for fruit in fruits:
        if item == fruit:
            print("calories: ", fruits[fruit])
    return

main()
# case insensitive
# returns nothing if no match