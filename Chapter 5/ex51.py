#Define and set variable
def get_day_name(day):

#Find and print day
    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    else:
        print("Not a valid number!")
#Run Function
get_day_name(day = int(input("Input value: ")))