#Evaluates a postfix expression and returns the final solution

from mystack import Stack
import string

def posteval(expr):
	operandstack = Stack()
	for i in expr.split():
		if i in string.digits:
			operandstack.push(int(i))
		else:
			sec = operandstack.pop()
			fis = operandstack.pop()
			res = eval('%d%s%d'%(fis,i,sec))
			operandstack.push(res)
	return operandstack.pop()

print posteval('7 8 + 3 2 + /')
