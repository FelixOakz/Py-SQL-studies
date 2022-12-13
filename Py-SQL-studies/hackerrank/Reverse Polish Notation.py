
def rpn(case):
	stack = []
	for i in case:
		if i.isnumeric():
			stack.append(int(i))
		elif i in "+-*/":
			n1 = stack.pop()
			n2 = stack.pop()
			if i == '+':
				stack.append(n1 + n2)
			elif i == '-':
				stack.append(n1 - n2)
			elif i == '*':
				stack.append(n1 * n2)
			elif i == '/':
				stack.append(n1 / n2)
	return stack.pop()