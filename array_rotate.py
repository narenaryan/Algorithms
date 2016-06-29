"""
A procedure for roatating a list in anti-clockwise direction by given number of turns
Ex: rotateArray([1,2,3,4,5], 2) => [3,4,5,1,2]
"""

def rotateArray(self, a, b):
    length = len(a)
    if b < length:
        return a[b:] + a[:b]
    else:
        mod = b % length
        return a[mod:] + a[:mod]    
