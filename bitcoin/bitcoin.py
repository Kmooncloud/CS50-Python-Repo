# pset4 Bitcoin Price Index
# returns the current price of command-line input n of bitcoin

import sys
import requests
import json

def main():
    n = float(get_n())
    ans = get_rate(n)
    print(f"${ans:,.4f}")

def get_rate(n):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") # API URL
    except requests.RequestException:
        sys.exit("Requests error")
    o = response.json()
    rate = o["bpi"]["USD"]["rate"]
    rate = float(rate.replace(",", ""))
    ans = rate * n
    return ans

def get_n():
    try:
        n = sys.argv[1]
    except IndexError:
        sys.exit("Missing command-line argument")
    try:
        n = float(n)
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return n

if __name__ == "__main__":
    main()