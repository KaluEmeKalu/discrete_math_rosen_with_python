# Python Implementation of Bubble Sort

a = [483,329,42,85,372]
# a = [1, 2, 4, 6, 8, 10]
n = len(a)

for i in range(1, n -1):
	switch_made = False
	for j in range(n - i):
		if a[j] > a[j + 1]:
			a[j], a[j + 1] = a[j+1], a[j]
			switch_made = True
	if not switch_made:
		print("You saved {} iteration".format(str(n - 1 - i)))
		break

print(a)



