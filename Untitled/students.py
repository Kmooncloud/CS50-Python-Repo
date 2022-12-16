import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])  #allows for diff ordering
    writer.writerow({"name": name, "home": home})


# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)   #loads in each line as a dict of columns
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):  # sort list of dict by studnets name
#     print(f"{student['name']} is from {student['home']}")


# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):  # sort list of dict by studnets name
#     print(f"{student['name']} is from {student['home']}")


# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")  # returns a list with 2 assigned values
#     # split returns a list of the values on the row divided by designated ""
#         print(f"{name} is in {house}")