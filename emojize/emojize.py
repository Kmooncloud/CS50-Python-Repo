# pset4 Emojize 
# takes ASKII input for an emoji and outputs the graphic emoji equivalent 

import emoji
import sys

word = input("Input: ")
print(emoji.emojize("Output: " + word, language="alias"))
