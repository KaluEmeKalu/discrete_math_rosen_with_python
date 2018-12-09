def f(integers):
    duplicates = []
    n = len(sample_list)
    x = 1
    while x < n:
        if integers[x] == integers[x - 1]:
            duplicates.append(integers[x])
            while x<n and integers[x] == integers[x - 1]:
                x = x + 1
                print(x)
        x = x + 1
    return duplicates

sample_list = [3,4,7,7,8,8,10,11,15,29,29,29,30]
print(f(sample_list))


