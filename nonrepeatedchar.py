def nonrepeated(s):
    charcount = {}
    for char in s:
        charcount[char] = charcount.get(char,0)+1
    for char in s:
        if charcount[char]==1:
            return char
    return None
s = "atyta"
print(nonrepeated(s))

