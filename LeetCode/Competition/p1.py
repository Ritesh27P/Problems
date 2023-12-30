def combinations(l):
    if l:
      result = combinations(l[:-1])
      return result + [c + [l[-1]] for c in result]
    else:
      return [[]]

print(len(combinations([1, 2, 3, 4, 5])))