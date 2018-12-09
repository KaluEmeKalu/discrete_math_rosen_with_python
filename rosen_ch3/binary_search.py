from math import floor

a = [1, 2, 3, 5, 6, 7, 8, 10 ,13, 15, 16, 18, 19, 20, 22]
x = 19
n = len(a)

i = 1
j = n

while i < j:
	m = (i + j) / 2
	m = floor(m)

	if x > a[m]:
		i = m + 1
	else:
		j = m

if x == a[i]:
	location = i
else:
	location = 0
print(location)