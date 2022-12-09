# pset5 Refueling
# output % between 2% - 98%
# output F at >= 99% and E at <= 1%
# with test
import sys


def main():
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        main()
    percentage = convert(fraction)
    sys.exit(f"{gauge(percentage)}")

def convert(fraction):
    # takes a string in format "x/y" and returns int between 0 -100
    percentage = int()
    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
    except (ValueError):
        raise ValueError
        main()
    try:
        percentage = (x/y) * 100
        return percentage
    except (ZeroDivisionError):
        raise ZeroDivisionError
        main()

def gauge(percentage):
    if 100 >= percentage >= 99:
        return f"F"
    elif percentage <= 1:
        return f"E"
    elif percentage > 100:
        main()
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()

