name = input("What's your name? ")

match name:
    case "Harry" | "Hermine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# Original idea
"""
if name == "Harry" or name == "Herminoe" or name == "Ron":
    print("Gryffindor")
elif name == "Draco"
    print("Slytherin")
else:
    print("Who?")
"""