def removeduplicates(arr):
    n = len(arr)
    if n<=1:
        return n
    index = 1
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            arr[index] = arr[i]
            index+=1
    return index
if __name__ == "__main__":
    arr = [1,1,2,2,3,3,3]
    newsize = removeduplicates(arr)
    for i in range(newsize):
        print(arr[i],end = ' ')