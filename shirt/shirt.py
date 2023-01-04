from PIL import Image, ImageOps
import sys
from os.path import splitext

def main():
    check_argv()
    put_a_shirt_on_it()

def check_argv():
    # checks for 3 commandline arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line argumets")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")
    # check for only .png or .jpg file types
    ext1 = splitext(sys.argv[1])
    ext2 = splitext(sys.argv[2])
    if check_ext(ext1[1]) == False:
        sys.exit("Invlaid input")
    elif check_ext(ext2[1]) == False:
        sys.exti("Invalid output")
    # check that before and after file types match
    if ext1[1].lower() != ext2[1].lower():
        sys.exit("Input and output have different extensions")
    # checks for file-not-found
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    return

def check_ext(file):
    if file not in [".jpg", ".jpeg", ".png"]:
        return False

def put_a_shirt_on_it():
    background = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    shirted = ImageOps.fit(background, size)
    shirted.paste(shirt, shirt)
    shirted.save(sys.argv[2])


if __name__ == "__main__":
    main()