# pset6 Pizza Py
# print out .csv file using tabulate formatting
import sys
import csv
from tabulate import tabulate


def main():
    check_argv_csv()
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

def check_argv_csv():
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
        if sys.argv[1].find(".csv") != -1:
            sys.exit("File does not exist")
        else:
            pass
    if sys.argv[1].find(".csv") == -1:
        sys.exit("Not a CSV file")
    else:
        return

if __name__ == "__main__":
    main()