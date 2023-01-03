import numpy as np

def strange_grid(c, r):
    # 0, 2, 4, 6, 8
    # 1, 3, 5, 7, 9
    # 10, 12, 14, 16, 18
    # 11, 13, 15, 17, 19
    # 20, 22, 24, 26, 28
    # 21, 23, 25, 27, 29
    even_r = [0, 2, 4, 6, 8]
    odd_r = [1, 3, 5, 7, 9]

    for i in range(r):
        print(np.array(even_r) + 10)
        print(np.array(odd_r) + 10)

# strange_grid(0, 4)

def strange_grid(r, c):
    even_r = [0, 2, 4, 6, 8]
    odd_r = [1, 3, 5, 7, 9]
    if r == 1:
        return even_r[c-1]
    if r == 2:
        return odd_r[c-1]
    if r == 3:
        return even_r[c-1] + 10
    if r == 4:
        return odd_r[c-1] + 10

    if abs(r-1)%2==0:
        return even_r[c-1] + (10 * (r-4))
    else:
        return odd_r[c-1] + (10 * (r-4))

print(strange_grid(16, 3))
print(strange_grid(4, 2))

def strangeGrid(r, c):
    return 10*((r-1)//2)+(r-1)%2+2*(c-1)