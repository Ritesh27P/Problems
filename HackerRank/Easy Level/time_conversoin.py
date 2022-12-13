#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour, minute, temp1 = s.split(':')
    hour, minute = int(hour), minute
    second, format = temp1[:2], temp1[2:]

    if format == 'AM':
        if hour == 12:
            hour = 0
    else:
        if hour == 12:
            pass
        else:
            hour += 12
    hour = str(hour)
    
    if len(hour) == 1:
        hour = f'0{hour}'


    return str(f'{hour}:{minute}:{second}')

        

print(timeConversion('07:05:45PM'))
