#Now rewrite the count_letters function so that instead 
# of traversing the string, it repeatedly calls the find 
# method, with the optional third parameter to locate 
# new occurrences of the letter being counted.

def count_let(text, let, pos=0):
    count = 0