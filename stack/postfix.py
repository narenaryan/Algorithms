from mystack import Stack
import string

#operator priority map
prior = {'+':0,'-':0,'*':1,'/':1}

#postfix function
def postfix(expr):
	optstack = Stack()
	olist = []
	for i in expr.split():
		if i is '(':
			optstack.push(i)
		elif i in string.uppercase or i in string.digits:
			olist.append(i)
		elif i is ')':
			while True:
				h=optstack.pop()
				if h == '(':
					break
				olist.append(h)
		elif i in prior.keys():
			if not optstack.isEmpty():
				if optstack.peek() == '(':
					optstack.push(i)
				else:
					while True:
						if not optstack.isEmpty():
							if prior[i]>prior[optstack.peek()]:
								optstack.push(i)
								break
							else:
								olist.append(optstack.pop())
						else:
							optstack.push(i)
							break
			else:
				optstack.push(i)

	if optstack:
		while not optstack.isEmpty():
			olist.append(optstack.pop())

	return ' '.join(olist)

#print postfix('A * B + C * D')
print postfix('( A + B ) * C - ( D - E ) * ( F + G )')
