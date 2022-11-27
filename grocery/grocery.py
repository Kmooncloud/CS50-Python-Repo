# pset3 Grocery List
# input grocery list items case-insensitive
# output alphabetized list, all caps, with the number of items according to identical input instances

def main():
    list = get_list()
    counts = get_count(list)
    for i in counts:    # prints in requested formatting: "value ITEM"\n
        print(counts[i], i.upper())

def get_list(): # gets a grocery list as input and stores in list
    list = []
    while True:
        try:
            i = input()
            i = i.lower()
            list.append(i)
        except EOFError:
            return list

def get_count(list):    # creates a dict to store number of repeated items and name together
    counts = {}
    for i in sorted(list):
        counts[i] = list.count(i)
    return counts


main()

