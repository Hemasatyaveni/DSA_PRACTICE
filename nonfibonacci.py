def nonfibonacci(n):
    fib = set()
    a,b = 0,1
    while a<=n:
        fib.add(a)
        a,b = b,a+b
    nonfib = []
    for i in range(1,n+1):
        if i not in fib:
            nonfib.append(i)
    return nonfib
print(nonfibonacci(20))