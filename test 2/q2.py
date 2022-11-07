list1 = [21,3,4,6,33,2,3,1,3,76,5]

def EvenVsOdd():
    even_count = 0
    odd_count = 0
    for num in list1:
        if num % 2 == 0:
            even_count += 1
    else:
        odd_count += 1
    print("Number of odd numbers:" , odd_count)

EvenVsOdd()