#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    # print(arr)
    # arr[0][0:3] + arr[1][1] + arr[2][0:3]
    # arr[0][1:4] + arr[1][2] + arr[2][1:4]
    # arr[0][2:5] + arr[1][3] + arr[2][2:5]
    
    row_11 = 0
    row_2 = 1
    row_13 = 3
    largest_hourglass = -100
    for iter in range(4):
        for i in range(4):
            value = (sum(arr[iter][(row_11+i):(row_13+i)])+
                arr[iter+1][row_2+i]+
                sum(arr[iter+2][row_11+i:row_13+i]))
            if value > largest_hourglass:
                largest_hourglass = value
    
    return largest_hourglass
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
