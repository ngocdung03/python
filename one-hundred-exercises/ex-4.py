def calculate(n):
    i = 2
    factors = []
    while i^2 <= n:
        if n % i != 0:
            i += 1
        else: 
            n = n // i 
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors   

print(calculate(20))