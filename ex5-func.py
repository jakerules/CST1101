#Define Variables
p=10000
n=12
r=.08
t=float(input("Enter year ammount: "))

#Function Definitions
def interest(p,r,t,n):
    return (p*((1+(r/n))*(n*t))) #DONT FOORGET OPERATOR!!!!
#Print
result = interest
print("Your new balence is: " , interest(p,r,t,n))