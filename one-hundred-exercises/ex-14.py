# Ex 14: return digit and times of repetitive*dot as a string

def compress(n):
    result = []
    str_n = str(n)
    count = 1
    element_pair = ''.join((str_n[0], '.'*count))
   
    for i in range(1, len(str_n)):
        if str_n[i] == str_n[i-1]:
            count += 1
            element_pair = ''.join((str_n[i], '.'*count))
        else:
            result.append(element_pair)
            count = 1
            element_pair = ''.join((str_n[i], '.'*count))
           
    result.append(element_pair)
   
    return "".join(result)
   
print(compress(1211))


# from itertools import groupby
 
 
# def compress(number):
#     result = []
#     for key, group in groupby(str(number)):
#         result.append((key, len(list(group))))
#     result = [''.join((i, '.' * j)) for i, j in result]
#     return ''.join(result)
   
   
# from itertools import groupby
 
 
# def compress(number):
#     result = [''.join((key, '.' * len(list(group)))) for key, group in groupby(str(number))]
#     return ''.join(result)
