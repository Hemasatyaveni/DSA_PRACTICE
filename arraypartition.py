def arraypartation(num):
    num.sort()
    n = len(num)//2
    count = 0
    for i in range(0,n*2,2):
        count+=num[i]
    return count
print()