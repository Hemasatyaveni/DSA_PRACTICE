 # def twosum(num,target):
#     nummap = { }
#     for i,val in enumerate(num):
#         complement = target - val
#         if  complement in nummap:
#             return [nummap[complement],i]
#         nummap[val] = i
# num = [2,3,4,7]
# target = 9
# print(twosum(num,target))
def twosum(num,target):
    nummap = {}
    for i in range(len(num)):
        val = num[i]
        complement = target-val
        if complement in nummap:
            return[nummap[complement],i]
        nummap[val]=i
num = [12,1,2,3]
target =14
print(twosum(num,target))

