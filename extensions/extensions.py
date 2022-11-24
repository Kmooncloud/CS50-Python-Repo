# pset1 File Extensions
# Inform user of file type

# request media type
media = input("File name: ")

# clean up input
media = media.lower().strip()

# output media type information
if media.find(".gif") != -1:
    print("image/gif")
elif media.find(".jpg") != -1:
    print("image/jpeg")
elif media.find(".jpeg") != -1:
    print("image/jpeg")
elif media.find(".png") != -1:
    print("image/png")
elif media.find(".pdf") != -1:
    print("application/pdf")
elif media.find(".txt") != -1:
    print("text/plain")
elif media.find(".zip") != -1:
    print("application/zip")
else:
    print("application/octet-stream")