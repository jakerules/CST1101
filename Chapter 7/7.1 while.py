def count_odd(n):
    #print(n)
    total= 0
    y = 0
    
    while y < len(n):
        if n[y] % 2 != 0:
            #print("I am at" , y , n[y])
            total = total + n[y]
        #print ("I am at list index" ,y," whihc has memebr" ,n[y] ,"curent total = ",total)
        y = y + 1
        #print("############################################")
    return total

print(count_odd([3,5,6,7,10]))