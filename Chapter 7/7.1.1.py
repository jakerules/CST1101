lst = [0, 4, 6, 9, 2, 3, 1]

def countOdds(l):
    count_odd = 0
    for num in l:
        if num % 2 != 0:
            count_odd = count_odd + 1
    return count_odd

print(countOdds(lst))


#Count amount of even numbers
count_even = len([num for num in lst if num % 2 != 0])

print(count_even)