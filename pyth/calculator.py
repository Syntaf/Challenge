#perform calculations on expressions entered in POSTFIX notation

while True:
	print("Enter your expression in POSTFIX Notation(q to quit): ")
	expression = input()
	vars = expression.split()
	if vars[0] == "q":
		break
	if len(vars) != 3:
		print("Invalid expression, correct format is: x y op")
	else:
		print("Solving:",vars[0], vars[2], vars[1])
		result = {
			"+" : lambda x, y: x + y,
			"-" : lambda x, y: x - y,
			"*" : lambda x, y: x * y,
			"/" : lambda x, y: x / y,
			"%" : lambda x, y: x % y
		}[vars[2]](int(vars[0]), int(vars[1]))
		print("Result:",result)
