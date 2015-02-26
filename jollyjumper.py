#!/usr/bin/python
import sys

fil = sys.argv[-1]

with open(fil,'r') as f:
    arr = [i.rstrip() for i in f.readlines()]
    for item in arr:
        final = [int(i) for i in item.split()]
        rev,temp = final[::-1],None
        if len(rev) == 1:
            print 'Jolly'
        else:
            for i,j in enumerate(rev):
                try:
                    check = abs(j - rev[i+1])
                    if i+1 != check:
                        temp = None
                        break
                except:
                    temp = i
            
            if temp:
                print 'Jolly'
            else:
                print 'Not jolly'
