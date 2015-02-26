#!/usr/bin/python
import sys


def gen_prime(n):
    size = n//2
    nsieve,limit = [1]*size,int(n**0.5)
    for i in range(1,limit):
        if nsieve[i]:
            gval = 2*i+1
            tmp = ((size-1) - i)//gval 
            nsieve[i+gval::gval] = [0]*tmp
    return nsieve

fil = sys.argv[-1]

with open(fil,'r') as f:
    arr = [i.rstrip() for i in f.readlines()]
    for item in arr:
        print ','.join([str(x) for x in iter([2] + [i*2+1 for i, v in enumerate(gen_prime(int(item))) if v and i>0])])
