def tuition():
    cost = 10000
    year = 0
    newcost = 10000
    peryear = .05
    while year < 10:
        newcost = newcost * peryear + newcost
        year = year + 1
        print(newcost)
    if year == 10:
        totalcost = newcost * 4
        print("The cost of tuition for 4 years, after 10 years, is: $", int(totalcost))
        return cost
tuition()