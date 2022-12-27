n = 20
loop = 0

for i in range(2, 100000):
    print(i)
    for j in range(1, n+1):
        if i%j == 0:
            loop += 1
    if loop == n:
        print(i)
        break
    loop = 0