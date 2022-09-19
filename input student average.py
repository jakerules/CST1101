#! Find Average for 5 Students
from audioop import avg
# Gather grades for students
stu1 = int(input("Enter student 1's grade: "))
stu2 = int(input("Enter student 2's grade: "))
stu3 = int(input("Enter student 3's grade: "))
stu4 = int(input("Enter student 4's grade: "))
stu5 = int(input("Enter student 5's grade: "))
# Sum the grades for students
sum = stu1 + stu2 + stu3 + stu4 + stu5
# Divide by number of Students
avg = sum / 5
# Display averages for students
print("The average for the students is" , avg)