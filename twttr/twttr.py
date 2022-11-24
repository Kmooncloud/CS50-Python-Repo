# pset2 Just setting up my twttr
# Takes string input and remove all vowels

def main():
    n = input("Input: ")
    remove_vowel(n)

def remove_vowel(n):
    # for every letter in n, if it's a vowel, remove it
    for p in n:
        if p.casefold() in ["a", "e", "i", "o", "u"]:
            print("", end="")
        else:
            print(p, end="")
        # on the last iteration print a new line?

main()
print("\n")