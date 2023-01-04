# pset6 Scourgify
# reads a file in Last, First, hosue format and writes a CSV in First, Last, House format
import csv
import sys

def main():
    check_argv()
    first_last()
    sys.exit()

def check_argv():
    # check the argv input is the name of an available python program no more, no less
    try:
        sys.argv[1]
        sys.argv[2]
    except IndexError:
        sys.exit("Too few command-line argumets")
    try:
        sys.argv[3]
        sys.exit("Too many command-line arguments")
    except IndexError:
        pass
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        if sys.argv[1].find(".csv") != -1:
            sys.exit(f"Could not read {sys.argv[1]}")
        else:
            pass
    if sys.argv[1].find(".csv") == -1:
        sys.exit("Not a CSV file")
    else:
        return

def first_last():
    students = []

    # read before.csv and copy information to memory
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

    # organize A = last B = first C = house
    ordered = []
    for row in students:
        last, first = row["name"].split(",")
        first = first.lstrip()
        house = row["house"]
        ordered.append({"first": first, "last": last, "house": house})

    # write to new CSV file with 3 columns first,last,house
    with open(sys.argv[2], "w+") as result:
        writer = csv.DictWriter(result, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for i in ordered:
            writer.writerow({"first": i["first"], "last": i["last"], "house": i["house"]})

if __name__ == "__main__":
    main()
