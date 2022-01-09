def calculate():
    list = []
    for n in range(100,1000):
        if n//100 == n%10:
            list.append(n)
    return list

print(len(calculate()))