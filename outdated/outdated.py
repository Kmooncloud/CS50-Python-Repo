# pset3 Outdated
# accept inputs formatted as "11/26/2022" or "November 26, 2022"
# and output ISO formatting "YYYY-MM-DD"
# do not accept other formats and continuously reprompt until valid input

# NOTE: this program is a mess. It would benefit immensely from being compeltely re-written.
#   Submitted due to time constraints with the intention or re-writing after class is completed

str_month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = input("Date: ")
    try:
        m, d, y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if d <= 31 and m <= 12:
            print(f"{y}-{m:02}-{d:02}")
        else:
            main()
    except ValueError:
        clean_up(date)


def clean_up(date):
    date = date.split()
    try:
        y = date[2]
        y = int(y)
        d = date[1]
    except (ValueError, IndexError):
        main()

    for i in str_month: # set m = to the index number in str_month list
        if i == date[0]:
            date[0] = str_month.index(i)
            m = date[0] + 1
            m = int(m)

    if not d.isdecimal():   # catch missing comma error, if no comma, reprompt user
        d = d.rstrip(',')
        try:
            d = int(d)
        except ValueError:
            main()
    else:
        main()

    if int(d) <= 31 and int(m) <= 12:
        print(f"{y}-{m:02}-{d:02}")
    else:
        main()


main()