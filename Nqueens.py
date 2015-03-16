#Program that prints all possible Nqueen soutions in a n*n chess board
#usage:  start_queening(0,n) where n is the row count of chess board '4' , '8' etc..

x,solutions = [],[]

def start_queening(pos,n):
	global x
	#create empty array to hold None values
	x = [None for i in xrange(n)]
	Nqueens(pos,n)


def Place(k,i):
	#Check whether kth queen can be placed on ith column
	global x
	for j in xrange(0,k):
		if x[j] == i or (abs(x[j] - i) == abs(j-k)):
			return False
	return True



def Nqueens(k,n):
	#Recursive solution for Nqueens
	global x,solutions
	for i in xrange(n):
		#If placable, then place
		if Place(k,i):
			x[k] = i
			#If queens exhausted,return solution
			if k == n-1:
				print x
			#Else start a new problem with queen placed in next column
			else:
				Nqueens(k+1,n)

#Start placing queens at 0th column
start_queening(0,8)
