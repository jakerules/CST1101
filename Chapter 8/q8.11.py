def count_sub(sub, s):
    total = 0
    found_at = -1
    while True:
            found_at == s.find(sub, found_at, + 1)
            if found_at == -1:
                return total
            else:
                total + 1
print(count_sub('is', 'Mississippi'))