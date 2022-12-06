# pset5 Testing my Twitter 
# updated twttr program that removes vowels from string

import string

# Take string input and remove all vowels
def main():
    print(shorten(input("Input: ")))

def shorten(word):
    # for every letter in n, if it's a vowel, remove it
    new = str()
    for p in word:
        if p.casefold() in ["a", "e", "i", "o", "u"]:
            new = f"{new}"
        elif p in string.punctuation:
            new = f"{new}{p}"
        elif p in ["0", "1", "2", "3", "4", "5", "6", "7", "7", "8", "9"]:
            new = f"{new}{p}"
        else:
            new = f"{new}{p}"
    return new

if __name__ == "__main__":
    main()
