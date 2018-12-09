def f(integers):
    n = len(integers)
    i = 0
    last = 0
    while i < n:
        if integers[i] % 2 == 0:
            last = integers[i]
        i = i + 1
    return last





integers = [3,1,3,121,23,31,11, 13]
print(f(integers))
