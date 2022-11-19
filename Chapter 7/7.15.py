def num_even_digits(n):
    n = str(n)
    list_even = ["0", "2", "4", "6", "8"]

    count = 0
    for char in n:
        if char in list_even:
            count += 1
    return count

num_even_digits(46521988795)