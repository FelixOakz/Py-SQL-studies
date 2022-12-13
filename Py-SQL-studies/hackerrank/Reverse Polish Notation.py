def rpn(cases):
	results = []
	for case in cases:
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
		# Check if the stack has exactly one element,
		# which should be the result of the calculation
		if len(stack) != 1:
			results.append("NO")
		else:
			results.append(stack.pop())
	return results


if __name__ == '__main__':
	cases = input()

	rpn(cases)