# pset1 Math Interpreter
# simple calculator
# future edits should include style updates
# and inclusion of a failsafe for accidental x/0

# recieve str input and convert to float
def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)

    # perform calculation
    if y == "+":
        answer = x + z
    elif y == "-":
        answer = x - z
    elif y == "*":
        answer = x * z
    else:
        answer = x / z
    print(round(answer, 1))

main()