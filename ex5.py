#Define Variables
p=10000
n=12
r=.08
t=int(input("Enter year ammount: "))

#Function Definitions
def interest(p,r,t,n):
    print(p((1+(r/n))(n*t)))
print("Your new balence is: " , interest)