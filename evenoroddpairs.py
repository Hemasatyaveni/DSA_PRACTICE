def evenorodd(arr,d):
    n = len(arr)
    d = d%n
    if n%2!=0:
        return arr[d:] + arr[:d]
    even = 0
    odd = 0
    for i in range(n):
        if arr[i]%2 ==0:
            even+=1
        else:
            odd+=1
    return (even//2)+(odd//2)
arr= [8,2,1,3,5]
d = 2
print(evenorodd(arr,d))