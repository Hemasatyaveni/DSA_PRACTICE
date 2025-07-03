def kthchar(k):
    word = "a"
    while len(word) < k:
        next = ''.join(
            chr((ord(c)-ord('a')+1)%26+ord('a'))
            for c in word
        )
        word+=next
    return word[k-1]
k = 5
print(kthchar(k))




