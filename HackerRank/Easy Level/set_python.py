n = int(input())
s = set(map(int, input().split()))

lp = int(input())
for i in range(lp):
    temp = input()
    if temp[0] == "p":
        s.pop()
    else:
        query, number = temp.split()
        number = int(number)
        if query == "remove":
            s.remove(number)
        if query == "discard":
            s.discard(number)
        # print(temp)


print(sum(s))