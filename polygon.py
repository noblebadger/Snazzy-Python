#!/bin/python

import sys
from math import trunc

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
s = sum(a)

counter = int(0)
valid = False

def ammend(l):
    a[-1] /= float(2)
    a.append(int(round(a[-1])))
    a[-2] = trunc(a[-2])
   
while(not valid):
    a.sort()
    if (n == 3):
        if ((a[0]**2 + a[1]**2) == a[2]**2):
            valid = True
        else:
            ammend(a)
            counter += 1
            n += 1
    else:
        if ((all(a) == a[0]) or (a.count(a[0]) and a.count(a[-1]) == 2)):
            valid = True   
        else:
            ammend(a)
            counter += 1
            n += 1
                    
print(counter)
              
