# Pset3 Felipe's Taqueria
# Ask user for menu item 
# repormpt if input is not in menu, not a str, or is cntl-d

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main(): 
    order = ticket("Item: ")
    print("\n")

def ticket(prompt): 
    price  = 0.00
    while True:
        try:
            order = input(prompt)   # ask for input 
            order = order.title()   # adjust to title case to search dict
            price = float(price) + float(menu[order])  # gets price from dict and adds to toal
            print(f"${price:.2f}")  # prints with $0.00 formatting 
        except KeyError:
            pass    # reprompt if not in dict
        except EOFError:
            return  # end program if cntl-d is input 


main()