def count_substr(str, substr):
    count = 0
    for i in range(len(str) - len(substr) + 1):
        if str[i] == substr [i:i+len(substr)] == substr:
            count += 1
    return count

print(count_substr("Mississippi" , "is"))