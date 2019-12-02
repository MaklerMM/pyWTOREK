def silnia(n):
    w = 1
    if (n == 2):
        return n
    return n * silnia(n-1)
n = 6
print("%d!=%d" % (n, silnia(n)))
print(silnia(6))

def fibonacci(n):
    fibo = [0,1]
    while(len(fibo) < n):
        number = fibo[len(fibo)-1]+fibo[(len(fibo)-2)]
        fibo.append(number)
    return fibo

print(fibonacci(10))
print(fibonacci(25))
