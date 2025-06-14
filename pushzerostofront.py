def zerofront(arr):
    n = len(arr)
    result = [0]*n
    index = n-1
    for i in range(n-1,-1,-1):
        if arr[i]!=0:
            result[index] = arr[i]
            index-=1
    for i in range(n):
        arr[i]=result[i]
if __name__ == "__main__":
    arr = [9,0,7,0,6,0,4,0,1,0,0]
    zerofront(arr)
    for num in arr:
        print(num,end = ' ')

