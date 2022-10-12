#Define
xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

#Function Definition
def grade_scheme(mark):
    if mark >= 75:
        return "First"
    elif mark > 70:
        return "Upper Second"
    elif mark > 60:
        return "Second"
    elif mark > 50:
        return "Third"
    elif mark > 45:
        return "F1 Supp"
    elif mark > 40:
        return "F2"
    else:
        return "F3"
    
#Test your function by printing the mark and the grade for all the elements in the list.

for i in xs:
    print("Mark: " + str(i) + "    Grade: " + str(grade_scheme(i)))