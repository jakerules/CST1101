#Define


x = int(input("Enter number 1"))
y = int(input("Enter number 2"))

a = -1
b = -1
#num1 calculation
def part1(x, y, a, b):
    if x > y:
        maxix = x
        print("num1 is max")
        return maxix
        a = 1
    elif x < y:
        print("num1 is min")
        a = 0
    else:
        print("Invalid")

    if y > x:
        maxiy = y
        b =1
        print("num2 is max")
        return maxiy
    elif y < x:
        miniy = y
        print("num2 is min")
        b = 0
    else:
        print("Invalid")
part1(x, y, a, b)
print(a, b)


