# pset5 Back to the Bank
# reimplemented version of Bank tested with test_bank.py

def main():
    greeting = input("Greeting: ")
    greeting = value(greeting)
    print(f"${greeting}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.find("hello") != -1:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()