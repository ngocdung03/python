# Ex 13: return digit and times of repetitive as a string

def compress(n):
    result = []
    str_n = str(n)
    count = 1
    element_pair = "".join((str_n[0], str(count)))
   
    for i in range(1, len(str_n)):
        if str_n[i] == str_n[i-1]:
            count += 1
            element_pair = "".join((str_n[i], str(count)))
        else:
            result.append(element_pair)
            count = 1
            element_pair = "".join((str_n[i], str(count)))
           
    result.append(element_pair)
   
    return "_".join(result)
   
print(compress(1211))


# from itertools import groupby
 
# def compress(number):
#     result = [''.join((key, str(len(list(group))))) for key, group in groupby(str(number))]
#     return '_'.join(result)