#Define Variables
print("Angle 3 is 90")
ang1 = float(input("What is angle 1: "))
ang2 = float(input("What is angle 2: "))

#Define function
#Define Function
def right(ang1, ang2):
    if ang1 + ang2 <= 90:   
        print("True")
    else:
        print("False")

#Check numbers and call if correct
if ang1 <=0 or ang2 <= 0:
    print("Numbers are - or 0")
elif ang1 + ang2 + 90 < 180:
    print("Numbers do not add up to 180 degrees")
elif ang1 + ang2 + 90 > 180:
    print("Numbers do not add up to 180 degrees")
else:
    right(ang1, ang2)
