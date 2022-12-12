def str_rev(s):
    i = -1
    rev = ""
    while i >= - len(s):
        rev = rev + s[i]
        i = i -1
    return rev

print(str_rev('Happy'))


def rmv_letter(ch, s):
    res = ""
    for i in s:
        if i != ch:
            res = res + i
    return res

print(rmv_letter('p','Happy'))

def pal(s):
    if str_rev(s) == s:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
    
pal("dad")
pal("Happy")