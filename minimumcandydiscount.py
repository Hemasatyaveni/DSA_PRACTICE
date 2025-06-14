# def candy(arr):
#     sum = 0
#     arr.sort(reverse = True)
#     for i in range(len(arr)):
#         if i%3!=2:
#             sum+=arr[i]
#     return sum
# arr = [1,2,3]
# print(candy(arr))

def candy(arr):
    sum = 0
    arr.sort(reverse = True)
    i = 0
    while i<len(arr):
        sum+=arr[i]
        if i +1 <len(arr):
            sum +=arr[i+1]
        i+=3
    return sum
arr = [1,2,3]
print(candy(arr))

