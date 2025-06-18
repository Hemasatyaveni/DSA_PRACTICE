def compressedstring(arr):
    n = len(arr)
    result = ""
    i = 0
    while i < n:
        count = 1
        while i+1 <n and arr[i]==arr[i+1]:
            count+=1
            i+=1
        result = result +arr[i] + str(count)
        i+=1
    return result
    # if len(result)<n:
    #     return result
    # else:
    #     return arr
arr = "a"
print(compressedstring(arr))
