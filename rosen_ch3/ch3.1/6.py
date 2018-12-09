def f(integers):
    n = len(integers)
    i = 0
    negative_list = []
    while i < n:
        if integers[i] <0:
            negative_list.append(integers[i])
        i = i + 1
    msg = f"There are {len(negative_list)} negative numbers"
    return msg, negative_list





integers = [3,-4,-2,121,23,-30]
print(f(integers))
print('s')