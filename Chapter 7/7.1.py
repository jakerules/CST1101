def odd():
    list = [23,56,89,45,6,78,9,4,97,49]
    numodd = 0
    for x in list:
        if x % 2 == 1:
            numodd += 1
        return numodd
odd()