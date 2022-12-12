def str_rev(s):
    i = -1
    res = ""
    while i >= - len(s):
        res = res + s[i]
        i = i -1
    return res

print(str_rev('Happy'))
