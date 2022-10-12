from ex51 import get_day_name
#Define
length = int(input("What is the number of days that passed?"))
day = (length % 7) + start

#print result

print(get_day_name(day))