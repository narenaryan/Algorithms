from mystack import Stack
#Finds whether given input paranthesis sequence is right or not.A stack application
s = Stack()

#((((()))))()

def check(expr):
	s = Stack()
	index =0 
	for i in expr:
		if i in '({[':
			s.push(i)
		elif i in ')}]':
			try:
				s.pop()
			except:
				return False
	if s.isEmpty():
		return True
	else:
		return False


print check('([{}])}')

