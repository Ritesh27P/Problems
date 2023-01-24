#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    ovels = ['a', 'e', 'i', 'o', 'u']
    
    highest_no_ovels = 0
    for i in ovels:
        if i in s:
            highest_no_ovels += 1
    
    if highest_no_ovels == 0:
        return "Not found!"
    
    st, lt = 0, k
    highest = 0
    highest_char = "Not found!"
    
    for i in range(len(s)-k):
        characters = s[st:lt]
        st += 1
        lt += 1

        char = 0
        for j in characters:
            if j in ovels:
                char += 1
                
        if char == k:
            return characters
        if highest_no_ovels == char:
            return characters
        elif char > highest:
            highest_char = characters
            highest = char
        
    return highest_char
        
            
            

        
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()
