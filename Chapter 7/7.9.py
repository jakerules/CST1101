def print_triangular_numbers(n):
    sum = 0
    for num in range(1, n+1):
        sum += num
        print(num, sum)
print_triangular_numbers(5)