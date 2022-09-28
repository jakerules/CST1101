#Get Info
current_time=int(input("What is the current time(Format 24hrs)"))
time_shift=int(input("How many hours"))
#Calculation and result
print("The time will be:", (current_time+time_shift)%24)