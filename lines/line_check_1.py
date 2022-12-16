# ask if an input number is even

def main():
    #get input
    n = input("Is it even: ")
    if n == True:
        print("Yes!")
    else:
        print("No :(")

# retun bool true if even
def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    main()

# has 10 lines of code