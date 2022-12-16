import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguemtns")

for arg in sys.argv[1:]:    # iterate over a list starting at location 1, not 0
    print("Hello, my name is", arg)


# Slives: takes a subset of a data structure
# Packages: third party libaries that can be installed
# pip: program manager allowing installation of 3rd party packages
# APIs : Application Programming Interface; a doorway throught which to access someone else's stored data and integrate into my own programs
# JSON: Javascript Object Notation

# Following checks if there are more than 2 elements in list and only prints out if a single input was written after calling the program
# import sys

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguemnts")

# print("Hello, my name is", sys.argv[1])

# sys.argv[] is a list of all input after program run in commandline