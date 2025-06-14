def pushzeroes(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count < len(arr):
        arr[count] = 0
        count+=1
    arr = [1,2,5,0,3,0]
    pushzeroes(arr)
    for num in arr:
        print(num,end = ' ')

    

