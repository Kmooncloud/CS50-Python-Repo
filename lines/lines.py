# pset6 Lines of Code
# get file name in commandline and return number of lines of code (not including comments)

import sys


def main():
    check_argv()
    print(count_lines())

def check_argv():
    # check the argv input is the name of an available python program no more, no less
    try:
        sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line argumets")
    try:
        sys.argv[2]
        sys.exit("Too many command-line arguments")
    except IndexError:
        pass
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        if sys.argv[1].find(".py") != -1:
            sys.exit("File does not exist")
        else:
            pass
    if sys.argv[1].find(".py") == -1:
        sys.exit("Not a python file")
    else:
        return


def count_lines():
    i = 0000
    with open(sys.argv[1]) as file:
        for l in file:
            l = l.strip()
            if l[:1] == "#":
                pass
            elif l.strip() == "":
                pass
            else:
                pass
                i += 1
    return i


if __name__ == "__main__":
    main()