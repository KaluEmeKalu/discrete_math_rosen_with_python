# Devise an algorithm that finds 
# the sum of all the integers in a list.


def _sum(integers):
	the_sum = 0 
	for x in integers:
		the_sum = the_sum + x
	return the_sum

print(_sum([3,1,2]))
