from ex51 import get_day_name
#Define
start = int(input("What is the starting day of the week number?"))
length = int(input("What is the number of days that passed?"))
day = (length % 7) + start

#print result

print(get_day_name(day))