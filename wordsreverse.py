def wordsreverse(n):
    words = n.split()
    a = [word[::-1] for word in words]
    b  = ' '.join(a)
    return b
n = 'i am good girl'
print(wordsreverse(n))

