
from string import ascii_letters, digits, punctuation
# giving access to all ascii characters, decimal digits and punctuation marks
from itertools import product
# habillity to cross product of all numbers

for passcode in product(ascii_letters + digits + punctuation, repeat=8):
	print(*passcode)
