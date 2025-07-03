def sumofsquares(n):
   
    sum = 0
    for i in n:
        sum+=i**2
    return sum
n = [1,2,3]
print(sumofsquares(n))
