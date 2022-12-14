# reads a file and prints out sorted contents of .txt file
names = []
with open("names.txt") as file:     # don't need to specify "r"
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")

# will also print a sorted version but will not allow
# for further manipulation of list from file in memory
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())


# can't iterate and print and sort in advance with this method
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# longer version:
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())

# writes a new .txt file with each input on a new line
# and automatically closes the file
# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# "w" will re-create the file