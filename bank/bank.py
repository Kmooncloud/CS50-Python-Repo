# pset1 Hope Federal Savings Bank
# Bank greeting compensation from Seinfeld skit 

# get greeting
greet = input("Greeting: ")

# clean up greeting
greet = greet.lower().strip()

# payout from greeting
if greet.find("hello") != -1:
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")