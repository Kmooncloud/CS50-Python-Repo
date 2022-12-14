# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("X is not an int ")
#     else:
#         break

# print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("X is not an int ")

# print(f"x is {x}")

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()