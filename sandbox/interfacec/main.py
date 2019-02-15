from pylibalex import alex_exponent, alex_sum

#
# Test the functions
#

#assert alex_exponent(5, 1.5) == 5**1.5
assert alex_exponent(5, 1.5) - 5**1.5 < 0.0001


L = [5, 6, 1.2, 7.8, 9.5]
assert alex_sum(L) == sum(L)


print("OK!")
