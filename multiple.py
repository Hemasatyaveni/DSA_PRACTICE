def multiple(n):
    if len(n)<2:
        return "no pattern"
    else:
        diff = n[1]-n[0]
        for i in range(2,len(n)):
            if n[i]-n[i-1]!=diff:
                return "no pattern"
                break
    return n[-1]+diff,diff
 
n = [0,3,6,9,12,15,18]
print(multiple(n))


