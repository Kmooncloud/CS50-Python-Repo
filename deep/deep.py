# pset1 Deep Thought
# Check if the user input includes some version of 42, else print no
# Answer to the the Great Question of Life

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# cleanup input
answer = answer.lower()
answer = answer.strip()

# check if answered correctly
match answer:
    case "42":
        print("Yes")
    case "forty two":
        print("Yes")
    case "forty-two":
        print("Yes")
    case _:
        print("No")