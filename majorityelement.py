def majorityelement(s):
    charcount = {}
    for char in s:
        if char in charcount:
            charcount[char]+=1
        else:
            charcount[char]=1
    result = []
    for char in charcount:
        count = charcount[char]
        if count>len(s)/3:
            result.append(char)
    return result
s = "1111122222"
print(majorityelement(s))
