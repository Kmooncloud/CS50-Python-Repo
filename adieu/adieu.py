# pset4 Adieu Adieu
# collect a list of names and print out according to correct grammar and punctuation
#import inflect  # It was easier for me to not use this package, I will try using it elsewhere

def main():
    names = []
    while True: # collect names for list until cntl-d
        try:
            n = input()
            names.append(n)
        except EOFError:
            break
    adieu(names)

def adieu(names):   # according the length of the list collected, print with correct punctuation
    if len(names) == 1:
        print("\nAdieu, adieu, to " + names[0])
    elif len(names) == 2:
        print("\nAdieu, adieu, to " + names[0] + " and " + names[1])
    elif len(names) > 2:
        print("\nAdieu, adieu, to ", end="")
        for i in names[0:-1]:
            print(i + ", ", end="")
        print("and " + names[-1], end="\n")
    else:
        main()

if __name__ == "__main__":
    main()