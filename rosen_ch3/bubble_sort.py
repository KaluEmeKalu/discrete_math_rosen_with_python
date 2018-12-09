a = [483,329,42,85,372]
n = len(a)

for i in range(1, n -1):
	for j in range(n - i):
		if a[j] > a[j + 1]:
			a[j], a[j + 1] = a[j+1], a[j]

print(a)