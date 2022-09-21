#Define Variables
p=10000
n=12
r=.08
t=float(input("Enter year ammount: "))

interest = (p*((1+(r/n))*(n*t)))

print(interest)