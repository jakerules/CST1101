def count_a(text):
    count = 0
    for c in text:
        if c == "a":
            count += 1
    return(count)

print(count_a("banana"))

def find2(string, ch, start):
    ix = start
    while ix < len(string):
        print("Position= " , ix, "Value= " , string)
        if string[ix] == ch:
            return(ix)
        ix += 1
    return(-1)
(find2("hipocratic", "a", 0))

