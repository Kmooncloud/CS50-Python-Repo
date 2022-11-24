# pset3 Fuel Gague 
# take a fraction input and output whole number % between 2% - 98%
# output F at >= 99% and E at <= 1%
# handle exceptions

def main():
    level = get_frac("Fraction: ")
    if level > 1:
        main()
    elif float(level) >= 0.99:
        print("F")
    elif float(level) <= 0.01:
        print("E")
    else:
        print(f"{int(round(level*100, 0))}%")

# Exceptions
# X or Y is not an int
# X is greater than Y [ if x%y > 1.0]
# Y is 0
def get_frac(prompt):
    while True:
        level = input(prompt)   # prompting the user is within the while True loop
        try:
            x, y = level.split("/")
            x = int(x)
            y = int(y)
            level = x/y
            return level
        except (ValueError, ZeroDivisionError):
            pass

main()
