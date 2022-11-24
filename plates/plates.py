# pset2 Vanity Plates
# Verify if a sumbission for vanity plates is valid under parameters

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    conditions = [lett_start(plate), two_six(plate), num_rule0(plate), num_rule1(plate), no_punct(plate)]
    return all(conditions)

def lett_start(plate):
    # Must start with 2 letters
    for n in plate[:2]:
        return isinstance(n, str)

def two_six(plate):
    # Between 2-6 chaaracters
    return 2 <= len(plate) <= 6

def num_rule0(plate):
    # no letters may follow numbers
    n = False
    for i in plate:
        if i.isdigit():
            n = True
        elif i.isalpha():
            if n == True:
                return False
    return True

def num_rule1(plate):
    # First number cannot be 0
    for n in plate:
        if n.isdigit():
            if n == "0":
                return False
            else:
                return True
    return True

def no_punct(plate):
    # No punctuation allowed
    from string import punctuation
    for i in plate:
        if i in punctuation:
            return False
    return True

main()