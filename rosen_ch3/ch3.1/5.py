# Describe an algorithm that takes as input a 
# list of n integers in nondecreasing order 
# and produces the list of all values that occur 
# more than once. (Recall that a list of integers is 
# nondecreasing if each integer in the list is at least as 
# large as the previous integer in the list.)
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


