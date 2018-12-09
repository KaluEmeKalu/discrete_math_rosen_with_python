def pro(x, exp):
	if exp == 1:
		return x
	if exp == 0:
		return 1
	if exp <=-1:
		return 1 / pro(x, exp * -1)
	if exp >=2:
		sum = x
		for i in range(2, exp + 1):
			sum = x * sum
		return sum


ans = pro(2,-4)
print(ans == 1 / (2 * 2 * 2 * 2))