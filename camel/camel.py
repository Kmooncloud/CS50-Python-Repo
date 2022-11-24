# pset2 camelCase 
# Take CamelCase input and output snake_case formatting

def main():
    camel = input("camelCase: ")
    snake_case(camel)
    print("")

#  add "_" before any capital letters
#  make everything lower case
def snake_case(camel):
    for c in camel:
        if c.islower():
             print(c, end="")
        else:
            print("_" + c.lower(), end="")   

main()