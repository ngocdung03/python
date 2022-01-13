# Ex 12: return digit and times of repetitive

def compress(n):
    result = []
    str_n = str(n)
    count = 1
    element_pair = (str_n[0], count)
   
    for i in range(1, len(str_n)):
        if str_n[i] == str_n[i-1]:
            count += 1
            element_pair = (str_n[i], count)
        else:
            result.append(element_pair)
            count = 1
            element_pair = (str_n[i], count)
           
    result.append(element_pair)
   
    return result
   
print(compress(1211))


# from itertools import groupby
 
# def compress(number):
#     return [(key, len(list(group))) for key, group in groupby(str(number))]

print([i for i in groupby(str(1211))])