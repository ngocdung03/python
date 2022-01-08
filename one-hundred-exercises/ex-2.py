def calculate(n):
    sum = 0
    for i in range(n):
        if i % 5 == 0 or i % 7 == 0:
            sum += i
    return sum

print(calculate(20))
print(calculate(100))