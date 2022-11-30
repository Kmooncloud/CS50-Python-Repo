# pset4 Frank, Ian and Glen's Letters
# accepts command line inputs for font selection and prints out requested input in 
# random or selected font from Figlet package

from pyfiglet import Figlet
figlet = Figlet()
import random
import sys

def main():
    if len(sys.argv) == 1:  # print in put in random font
        phrase = input("Input: ")
        i = random.choice(figlet.getFonts())   # get a random str value from the list of fonts
        figlet.setFont(font=i)
        print("Output: " + figlet.renderText(phrase))
    elif "-f" in sys.argv:    # print input in requested font
        try:
            figlet.setFont(font=sys.argv[2])
            phrase = input("Input: ")
            print(figlet.renderText(phrase))
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

main()


