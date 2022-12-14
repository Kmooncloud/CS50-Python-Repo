'''
#create a list of students, lists are 0 index'd
students = ["Hermione", "Harry", "Ron"]

# python initializes the variabe student by itself
for student in students:
    print(student)

# this loop will perform all indented code before moving i to the next place in the list
# and repeat until end
# len tells how long a list is
for i in range(len(students)):
    print( i + 1, students[i])

# dict associates keys: values
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep="- ")
'''

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep="- ")