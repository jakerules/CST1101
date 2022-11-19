def is_prime(x):
    divis = 0
    for i in range(2,x):
        if x % i == 0:
            divis += 1
        if divis > 0 and x != 1:
            return False
        else:
            return True
is_prime(567)