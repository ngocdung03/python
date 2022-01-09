# takes a natural number as an argument and checks if it is a prime number
def is_prime(n):
    if n <=1:
        return False
    else:
        for i in range(2, n): 
            if n % i == 0:
                return False
    return True


# def is_prime(n):
#     if n < 2:
#         return False
#     if n % 2 == 0:
#         return n == 2
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 2
#     return True

print(is_prime(0))
print(is_prime(11))