# for i in range(100, 1000):
#     for j in range(100, 1000):
#         if i*j == 792297:
#             print(i, j)

# print('hii')

# def largest_palindrome(n):
#     print(n)
#     n = str(n)
#     if n[:3] == n[3:]:
#         for i in range(100, 1000):
#             for j in range(100, 1000):
#                 if i*j == int(n):
#                     return n
#     n = str(int(n[:3]) -1)
#     n = n+n
#     return largest_palindrome(int(n)-1)


# # print("ans = ", largest_palindrome(800000))

# # n = 800000

# # for i in range(15):
# #     n = str(n)
# #     st_n = str(int(n[:3]) -1)
# #     st_nd = st_n + st_n[::-1]
# #     n = int(st_nd)
# #     print(n)

# def prev_palindrome(n):
#     n = str(n)
#     st_n = str(int(n[:3]) -1)
#     st_nd = st_n + st_n[::-1]
#     n = int(st_nd)
#     return n
    
# def reverse(s):
#     s = str(s)
#     return s[::-1]


# def largest_palindrome(n):
#     # print(n)
#     n = str(n)
#     if n[:3] == reverse(n[3:]):
#         n = int(n)
#         for i in range(100, 1000):
#             for j in range(100, 1000):
#                 if (i*j) == n:
#                     # print('hiii', i, j)
#                     return n

#     n = prev_palindrome(n)
#     return largest_palindrome(n)

# print(largest_palindrome(800000))

#!/bin/python3

import sys

def prev_palindrome(n):
    n = str(n)
    st_n = str(int(n[:len(n)//2]) -1)
    st_nd = st_n + st_n[::-1]
    return int(st_nd)
    
def reverse(s):
    s = str(s)
    return s[::-1]


def largest_palindrome(n):
    # print(n)
    n = str(n)
    if n[:3] != reverse(n[3:]):
        n = n[:3] + reverse(n[:3])

    # print(n)
    if n[:3] == reverse(n[3:]):
        n = int(n)
        for i in range(100, 1000):
            for j in range(100, 1000):
                if (i*j) == n:
                    return str(n)
    # print(n)
    n = prev_palindrome(n)
    return largest_palindrome(n)

def largest_palindrome(n):
    temp = str(n)
    if temp[:len(temp)//2] != reverse(temp[len(temp)//2:]):
        temp = temp[:len(temp)//2] + reverse(temp[:len(temp)//2])

    if int(temp) > n:
        return largest_palindrome(prev_palindrome(n))

    if temp[:len(temp)//2] == reverse(temp[len(temp)//2:]):
        for i in range(100, 1000):
            for j in range(100, 1000):
                if (i*j) == int(temp):
                    return temp

    return largest_palindrome(prev_palindrome(n))


# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print(largest_palindrome(n))


# prime_factor = [2, 3, 5, 7, 11, 13, 17, 23, 29]
# no = 101101

# for _ in range(100):
#     for i in prime_factor:
#         if no%i == 0:
#             no /= i
#             continue
#         if no == 1:
#             break

# print(prime_factor)

prime_number = [2, 3, 5]
for i in range(800000):
    if i%2==0 or i%3==0 or i%5==0:
        continue
    prime_number.append(i)
    
print(prime_number)
