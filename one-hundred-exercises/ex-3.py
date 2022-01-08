def calculate(n):
    # fib = list()
    sum, first, second = 0, 0, 1
    while first < n:
        if first % 2:
            sum += first
        first, second = second, first + second
    return sum

print(calculate(1000000))