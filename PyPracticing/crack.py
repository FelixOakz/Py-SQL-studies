from string import digits
# giving access to all decimal digits
from itertools import product
# habillity to cross product of all numbers

for passcode in product(digits, repeat=4):
	print(*passcode)