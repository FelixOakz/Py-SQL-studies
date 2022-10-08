"""
.     any character
.*    0 or more characters
.+    1 or more characters
?     optional
^     start of input
$     end of input
"""
import re as regularexpressions

s = input('Do you agree?: ').lower()
if regularexpressions.search("^y(es)?$", s):
	print('Agreed.')
elif regularexpressions.search("^no?$", s):
	print("Not agreed.")

