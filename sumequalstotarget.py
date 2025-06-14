# def sumtotarget(arr,target):
#     arr.sort()
#     left,right = 0 ,len(arr)-1
#     while left < right:
#         sum= arr[left]+arr[right]
#         if sum == target:
#             return True
#         elif sum<target:
#             left+=1
#         else:
#             right-=1
#     return False
# arr = [1,4,7,3,2,9]
# target = 80
# print(sumtotarget(arr,target))
def twosum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return True
    return False
if __name__ == "__main__":
    arr = [1,2,3,4]
    target= 3
    if twosum(arr,target):
        print("true")
    else:
        print("false")

