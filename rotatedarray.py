def rotateArr(arr, d):
    n = len(arr)
    # d = d % n 
    temp = arr[d:] + arr[:d]
    for i in range(n):
        arr[i] = temp[i]
arr = [1,2,3,4,5]
d = 2
rotateArr(arr, d)
print("Rotated array:", arr)
