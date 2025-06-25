def kminmax(arr,k):
    arr.sort()
    n = len(arr)
    min = arr[k-1]
    max = arr[n-k]
    return min,max
arr = [9,3,4,1,6,8]
k = 3
print(kminmax(arr,k))