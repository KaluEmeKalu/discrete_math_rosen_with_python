from math import floor

a = [1, 2, 3, 5, 6, 7, 8, 10 ,13, 15, 16, 18, 19, 20, 22]
x = 19

def binsearch(pylist, element):
    pylist = sorted(pylist) # Just to be sure
    if len(pylist) == 0:
        return False    

    if len(pylist) == 1:
        if pylist[0] == element:
            return True
        else:
            return False
    else:
        mid = len(pylist) // 2
        if element == pylist[mid]:
            return True
        elif element > pylist[mid]:
            return binsearch(pylist[mid:], element)
        else:
            return binsearch(pylist[:mid], element)


print(binsearch(a,x))