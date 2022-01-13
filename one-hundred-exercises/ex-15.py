# Ex 15: decompress the expression to a number

def decompress(s):
   
    number = []
   
    for i in range(len(s)):
        if int(i) % 3 == 0:
            element = s[i]*int(s[i+1])
            number.append(element)
        else:
            pass
       
    return int("".join(number))
   
# int("".join(number))
print(decompress('11_22'))

 
# def decompress(compressed):
#     result = [tuple(item) for item in compressed.split('_')]
#     result = [i * int(j) for i, j in result]
#     return int(''.join(result))
    
