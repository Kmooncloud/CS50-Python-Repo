# pset0 Making Faces
# return user input of a happy or sad face as an emoji

def main():
  vibe = input("How are you doing? ")
  convert(vibe)

def convert(face):
  face = face.replace(":)", "🙂")
  face = face.replace(":(", "🙁")
  print(face)

main()