list = [-3, -5, -9, 5, 78,98]

def count_negitive(list):
    for i in list:
        sum(i for i in list if i < 0)
print(count_negitive(list))