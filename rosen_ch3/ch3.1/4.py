def f(integers):
    max_diff = integers[0] - integers[1]

    n = len(integers)
    for i in range(n -1):
        diff = integers[i] - integers[i + 1]
        if diff > max_diff:
            max_diff = diff

    return max_diff


l = [3,6,4,10,-3,2]
print(f(l))
