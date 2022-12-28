#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    for i in range(1, n+1):
        sum += i
    
    sq_sum = 0
    for i in range(n+1):
        sq_sum += i*i
    print(abs(sum**2 - sq_sum))
