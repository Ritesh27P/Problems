import time
n = 5
arr = []
seq1 = []

for i in range(n//2):
    arr.append(2)
if n%2 == 1:
    arr.append(1)


while 2 in arr:
    print(arr)
    arr.remove(2)
    arr.append(1)
    arr.append(1)

print(arr)