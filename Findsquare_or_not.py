#Check whether given coordinates form square or not
'''
Input file format

file starts here
(1,6), (6,7), (2,7), (9,1)
(4,1), (3,4), (0,5), (1,2)
(4,6), (5,5), (5,6), (4,5)
file ends here
'''
import sys
from math import sqrt

def partize(l, n):
    for i in xrange(0, len(l), n):
        yield tuple(l[i:i+n])

fil = sys.argv[-1]
with open(fil,'r') as f:
    arr = [i.rstrip() for i in f.readlines() if i != '\n']
    for item in arr:
        first_pass = [i.lstrip('(').rstrip(')') for i in item.split(',')]
        second_pass = [int(i.lstrip(' (')) for i in first_pass]
        co_ords = (i for i in partize(second_pass,2))
        fis,sec,third,fourth = co_ords
        fis_to_sec = sqrt(((sec[1] - fis[1]) ** 2 ) + ((sec[0] - fis[0]) ** 2)) 
        fis_to_third = sqrt(((third[1] - fis[1]) ** 2 ) + ((third[0] - fis[0]) ** 2))
        fis_to_fourth = sqrt(((fourth[1] - fis[1]) ** 2 ) + ((fourth[0] - fis[0]) ** 2))

        if fis_to_sec == fis_to_third:
            sec_to_third = sqrt(((third[1] - sec[1]) ** 2 ) + ((third[0] - sec[0]) ** 2))
            if sec_to_third == fis_to_fourth:
                print 'true'
            else:
                print 'false'

        elif fis_to_sec == fis_to_fourth:
            sec_to_fourth = sqrt(((fourth[1] - sec[1]) ** 2 ) + ((fourth[0] - sec[0]) ** 2))
            if sec_to_fourth == fis_to_third:
                print 'true'
            else:
                print 'false'

        elif fis_to_third == fis_to_fourth:
            third_to_fourth = sqrt(((fourth[1] - third[1]) ** 2 ) + ((fourth[0] - third[0]) ** 2))
            if third_to_fourth == fis_to_sec:
                print 'true'
            else:
                print 'false'

        else:
            print 'false'
