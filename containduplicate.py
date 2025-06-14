def duplicate(num):
    n = len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i]==num[j]:
                return True
    return False
print(duplicate([1,2,3]))