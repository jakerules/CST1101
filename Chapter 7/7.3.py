def sumNegativeInts(userList):
    sum = 0
    for i in userList:
        if i < 0:
            sum += i
    return sum
print(sumNegativeInts([-25, 5, -24, 36, 87]))