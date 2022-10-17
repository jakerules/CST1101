#Define


x = int(input("Enter number 1"))
y = int(input("Enter number 2"))

#num1 calculation
def part1():
    if x > y:
        max = x
        min = y
    else:
        max = y
        min = x

print(part1(x, y))


