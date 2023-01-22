# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

n = int(input())

for i in range(n):
    query = input()
    if query[0] == 'p':
        funct = query
    else:
        funct, number = query.split()
        number = int(number)
    if funct == "append":
        d.append(number)
    elif funct == "appendleft":
        d.appendleft(number)
    elif funct == "pop":
        d.pop()
    elif funct == "popleft":
        d.popleft()
        
for i in d:
    print(i, end=" ")