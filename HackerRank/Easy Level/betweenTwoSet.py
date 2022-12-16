def factors(a):
    set1 = set()
    for i in range(a):
        for j in range(10):
            if (i * j) == a:
                set1.add(i)

    return set1


def intersectionSet(a, b):
    final_set = set()
    temp1 = set()
    x = [ temp1.add(i) for i in factors(a)]
    temp2 = set()
    x = [temp2.add(i) for i in factors(b)]
    intersect = temp1.intersection(temp2)
    final_set.update(intersect)
    print(intersect)

    return final_set

# print(factors(16))
# print(factors(32))
# print(factors(96))

# print()

# def getTotalX(a, b):
#     fset = set()
#     for i in factors(b[0]):
#         fset.add(i)
#     for i in range(1, len(b)):
#         tempset = factors(i)
#         fset.intersection(tempset)
    
#     return fset

# def getTotalX(a, b):
#     fset = set()

#     for i in range(1, len(b)):
#         set1 = intersectionSet(b[i-1], b[i])
#         fset.update(set1)
#     return len(fset);


# print(getTotalX([3, 4], [24, 48]))
# print()

# print(getTotalX([2, 6], [24, 36]))

def factors(a):
    set1 = set()
    for i in range(a):
        for j in range(10):
            if (i * j) == a:
                set1.add(i)

    return set1

print(factors(2))
print(factors(4), factors(16), factors(32), factors(96))
