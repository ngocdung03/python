# Ex 11: all three-digit palindromic numbers in both decimal and binary notation

def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]
   
def calculate():
   
    pal_three = []
   
    for number in range(100, 1000):
        if is_palindrome(number):
            pal_three.append(number)
           
    return pal_three

print(calculate())

# def calculate():
#     return [i for i in range(100, 1000) if is_palindrome(i)]

# def calculate():
#     return list(filter(is_palindrome, [i for i in range(100, 1000)]))