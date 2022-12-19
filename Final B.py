#Final CST1101
#Write a function that counts how many 
#times a substring occurs in a string.


#Get values
str = input("What is the String?")
substr = input("What is the substring to count?")

#Define Function
def count_substr(str, substr):
    count = 0
    for i in range(len(str) - len(substr) + 1):
        if str[i:i+len(substr)] == substr:
            count += 1
    return count

#Run function
count_substr(str, substr)