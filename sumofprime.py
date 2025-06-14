def sumofprime(n):
   
    if n <2:
        return False
    for num in range(2,n+1):
        for i in range(2,int(num**0.5)+1):
            if n%i==0:
                return False
    return False
print(sumofprime(9))