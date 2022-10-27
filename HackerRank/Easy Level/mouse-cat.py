#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cat_A = abs(x-z)
    cat_B = abs(y-z)
    if cat_A == cat_B:
        return 'Mouse C'
    if cat_A < cat_B:
        return 'Cat A'
    if cat_B < cat_A:
        return 'Cat B'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
