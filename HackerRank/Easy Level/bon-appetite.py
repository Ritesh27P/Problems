import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    bill.pop(k)
    total = 0;
    for i in bill:
        total += i;
    
    value = int(b - (total/2))
    if value == 0:
        print('Bon Appetit')
    else:
        print(value)
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
