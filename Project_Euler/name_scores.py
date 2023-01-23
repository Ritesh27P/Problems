score = lambda name: sum(map(lambda x: ord(x)-64, name))
names = sorted(input() for _ in range(int(input())))
hash = {n: i * score(n) for i, n in enumerate(names, 1)}
[print(hash[input()]) for _ in range(int(input()))]