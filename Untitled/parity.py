#Parity refers to even or odd
# % used to find the remainder after division

# Even or odd?

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# the MOST pythonic way
def is_even(n):
    return n % 2 == 0

# the pythonic way
# def is_even(n):
   # return True if n % 2 == 0 else False

"""
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
"""

main()