def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum == n:
        print("perfect")
    else:
        print("not perfect")
    return sum
    

print(perfect(8))
