from math import floor

a = [1, 2, 3, 5, 6, 7, 8, 10 ,13, 15, 16, 18, 19, 20, 22]
x = 19
n = len(a)

i = 1

while i <= n and x !=a[i]:
	i = i + 1
if i <= n:
	location = i
else:
	location = 0
print(location)