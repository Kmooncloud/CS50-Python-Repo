# Make a while loop that prints "meow" 3 times
'''
i = 3
while i != 0:
    print("meow")
    i = i - 1

# incrimental convention i += 1
i = 0
while i < 3:
    print("meow")
    i = i + 1

# initializes variables to 0 and prints throgh list range
for i in [0, 1, 2]:
    print("meow")

# name an "unused" variable _ for pythonic convention
for _ in range(3):
    print("meow")

#feature of multiplying a print statment
print("meow\n" * 3, end="")

# prompt user for input invoking infinite loop
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    # break breaks out of most recent loop

for _ in range(n):
    print("meow")
'''

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
#also possible to use break and return n outside of the loop
            # break
        # return n

def meow(n):
    for _ in range(n):
        print("meow")

main()