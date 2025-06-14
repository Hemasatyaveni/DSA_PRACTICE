def median(arr1,arr2):
    arr = arr1+arr2
    arr.sort()
    n = len(arr)
    mid1 = n//2
    mid2 = mid1 - 1
    result = (arr[mid1] + arr[mid2]) /2.0
    return result
arr1 = [3]
arr2 = [4]
print(median(arr1,arr2))
