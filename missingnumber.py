def missingno(num):
    # 1st code:
    # n = len(num)
    # expected = n*(n+1)//2
    # actual = sum(num)
    # missing = expected-actual
    # return missing
    # 2nd code
    # return sum(range(len(num)+1)) - sum(num)
    # 3rd code
    n = len(num)
    setnum = set(num)
    result = []
    for i in range(n+1):
        if i not in setnum:
            result.append(i)
    return result
print(missingno([0,1,2,4,5]))