# pset2 Coke Machine
# charge 50 at a vending machine for Coke and determine amount owed or change due 

def main():
    coke = 50
    print("Amount Due: ", coke)
    amount_due(coke)

def amount_due(coke):
    n = int(input("Insert Coin: "))
    # only accept if n = [1, 5, 10, 25]
    if n in [1, 5, 10, 25]:
        # Determine amount more to pay or change due
        coke = coke - n
        if coke > 0:
            print("Amount Due: ", coke)
            amount_due(coke)
        else:
            print("Change Owed: ", abs(coke))
    # Otherwise keep asking for input
    else:
        print("Amount Due:", coke)
        amount_due(coke)

main()