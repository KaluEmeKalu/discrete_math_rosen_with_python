def pro(x: int or float, exp: int):

	if type(4) != type(exp):
		return "Sorry, exp not an int"

	if exp == 0:
		total = 1
	elif exp < 0:
		total = 1 / pro(x, exp * -1)
	elif exp >= 2:
		total = x
		for i in range(2, exp + 1):
			total = x * total
	else:
		return ValueError(f'Cannot give you {x}^{exp}')
	
	if total != x**exp:
		msg = f"should be {x**exp}, but got {total} instead"
		return msg
	return total


x = pro(3,2.6)

print(x)

# import unittest
# class TestExponentProcedure(unittest.TestCase):


#     def test_postive_x_with_negative_exponent(self):
#         self.assertEqual(pro(2,-4), 2**-4)

#     def test_postive_x_with_postive_exponent(self):
#         self.assertEqual(pro(2,4), 2**4)


#     def test_negtaive_x_with_postive_exponent(self):
#         self.assertEqual(pro(-2,4), (-2)**4)


#     def test_negative_x_with_negative_exponent(self):
#         self.assertEqual(pro(-2,-4), (-2)**-4)



# unittest.main()