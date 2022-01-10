# determines the greatest common divisor of two numbers
def greatest_common_divisor(n1, n2):
    factor_n1 = []
    factor_n2 = []
    common_divisor = []
    for i in range(1, n1+1):
        if n1 % i == 0:
            factor_n1.append(i)
    for i in range(1, n2+1):
        if n2 % i == 0:
            factor_n2.append(i)
    for i in factor_n1:
        for j in factor_n2:
            if i == j:
                common_divisor.append(i)
    return max(common_divisor)

# def greatest_common_divisor(a, b):
#     while b:   #while b != 0 ?
#         a, b = b, a % b
#     return a

print(greatest_common_divisor(32,100))

