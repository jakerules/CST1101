x = int(input("Enter number 1"))
y = int(input("Enter number 2"))
z1 = -1
z2 = -1
max = -1
min = -1
def part1(x, y):
    if x > y:
        return x in max
    else:
        return y in min

print(min, max)
