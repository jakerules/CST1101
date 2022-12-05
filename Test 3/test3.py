#Write a function that will remove  Vowels  letters from any text . 
#Vowels are  "!\""aeiouAEIOU". Make sure that your function is 
#tested and work with different text examples.

def test():
    print("Do you want to use sample string or input a string?")
    choice = input("1 for example, 2 for user input")
    return choice
def rem_vowl(choice):
    #Get inital input
    if choice == "1":
        original = "Education is the foundation of all civil lib"
    #Define variables
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U', '!', '/')
    new = ""
    #Start removal
    for i in original:
        if i not in vowels:
            new = new + i
    #Return text without vowels
    return new
