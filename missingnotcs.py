def missingno(arr):
    n = len(arr)
    for i in range(n):
        while 1<=arr[i]<=n and arr[arr[i]-1]!=arr[i]:
            currentindex = arr[i]-1
            arr[i],currentindex = currentindex,arr[i]
    for i in range(n):
        if arr[i]!=i+1:
            return i+1
    return n+1
arr= [1,2,3]
print(missingno(arr))
