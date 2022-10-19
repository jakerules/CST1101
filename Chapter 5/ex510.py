#Define function
def find_hypot(ang1,ang2):
    return (ang1 ** 2 + ang2 ** 2) ** 0.05

#Define variables
ang1 = int(input("What is angle 1: "))
ang2 = int(input("What is angle 2: "))

#Call function with variables
ang3 = find_hypot(ang1, ang2)

#Print results
print("The hypotenuse is: " , ang3)