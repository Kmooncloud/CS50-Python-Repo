def main():   # run a test to make sure that the saved algorithms function as intended
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":  # main will not get called when inported as a library into another program
    main()