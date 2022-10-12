#Define and import
from ex51 import get_day_name
import ex51

day = ex51.Day
length = int(input("What is the number of days that passed?"))
#Calculate
day = (length % 7) + day

#print result
print(get_day_name(day))