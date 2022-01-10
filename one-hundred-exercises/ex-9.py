# returns a prime number at position 100
def is_prime(n):
    if n <=1:
        return False
    else:
        for i in range(2, n): 
            if n % i == 0:
                return False
    return True

def calculate(n):
    prime_list = []
    while i < n:
        
