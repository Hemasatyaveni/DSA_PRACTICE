def minmax(arr):
    minno = arr[0]
    maxno = arr[0]
    for num in arr:
        if num < minno:
            minno = num
        if  num > minno:
            maxno = num
    return minno,maxno
arr = [2,3,4,1]
print(minmax(arr))
