str = input("What is the String?")
substr = input("What is the substring to count?")

#Define Function
def count_substr(str, substr):
    count = 0
    for i in range(len(str) - len(substr) + 1):
        if str[i:i+len(substr)] == substr:
            count += 1
    return count

count_substr(str, substr)

