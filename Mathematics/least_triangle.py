# Given integers a and b, find the smallest integer , such that there exists a triangle of height , base , having an area of at least .

import math

def least_triangle(b, a):
    return math.ceil(a/(0.5*b))

print(least_triangle(2, 2))
print(least_triangle(17, 100))
print(least_triangle(4, 6))