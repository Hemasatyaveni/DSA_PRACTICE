def removeoccurance(arr,a):
    k = 0
    for i in range(len(arr)):
        if arr[i]!=a:
            arr[k] = arr[i]
            k+=1
    return k
if __name__ == "__main__":
    arr = [1,2,3,4,5,8,2,6,7]
    a = 2
    print(removeoccurance(arr,a))