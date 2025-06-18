def minhousesrequired(r,unit,arr):
    required = r*unit
    sum = 0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum>=required:
            return i+1
    return -1
r = 7
unit = 2
arr = [2,8,3,5,7,4,1,2]
print(minhousesrequired(r,unit,arr))