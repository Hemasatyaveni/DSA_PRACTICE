# def onetrans(arr):
#     n = len(arr)
#     result = 0
#     for i in range(n-1):
#         for j in range(i+1,n):
#             result= max(result,arr[j]-arr[i])
#     return result
# arr = [7, 10, 1, 3, 6, 9, 2]
# print(onetrans(arr))
def onetrans(prices):
    n = float('inf')
    result =0
    for price in prices:
        n = min(n,price)
        result = max(result,price- n)
    return result
prices = [7, 10, 1, 3, 6, 9, 2]
print(onetrans(prices))