'''
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")
# alt
#   print("#\n" * height, end="")

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("+", end="")
        print()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)


main()
'''

#vary size of shape
def main():
    print_shape(3)

def print_shape(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)


main()