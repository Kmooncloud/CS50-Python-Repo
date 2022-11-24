# pset1 Meal Time
# Inform user of what meal to eat according to the time of day input

def main():
    time = input("What time is it? ")
    convert(time)

# convert time to floats
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    # convert minutes to decimal place and add back to hours
    minutes = minutes/60
    time = hours + minutes

    # time to meal
    if 7.0 <= time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= time <= 13.0:
        print("Lunch time")
    elif 18.0 <= time <= 19.0:
        print("Dinner time")
    else:
        return(time)
        #somehow return false

#if _name_ == "_main_": #why is this an if to run main()?
main()