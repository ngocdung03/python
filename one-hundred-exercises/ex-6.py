def calculate():
    palindromic = []
    
    for i in range(10,100):
        j = 10
        while j < 100:
            product = i*j
            j += 1
            if str(product)[0] == str(product)[-1] and str(product)[1] == str(product)[-2] and str(product)[2] == str(product)[-3]:      # str(i * j) == str(i * j)[::-1]
                palindromic.append(product)
            
    return palindromic

# def calculate():
#     result = max([i * j
#                   for i in range(10, 100)
#                   for j in range(10, 100)
#                   if str(i * j) == str(i * j)[::-1]])
#     return result
 

print(calculate())
