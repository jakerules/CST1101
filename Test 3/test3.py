#Write a function that will remove  Vowels  letters from any text . 
#Vowels are  "!\""aeiouAEIOU". Make sure that your function is 
#tested and work with different text examples.

def rem_vowl():
    #Get inital input
    original = "Education is the foundation of all civil liberties"
    #Define variables
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U', '!', '/')
    new = ""
    #Start removal
    for i in original:
        if i not in vowels:
            new = new + i
    #Return text without vowels
    return new

rem_vowl()
