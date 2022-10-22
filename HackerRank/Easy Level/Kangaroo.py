def kangaroo(x1, v1, x2, v2):
    if v1==v2:
        return "NO"
    intersect = (x1-x2)/(v2-v1)
    if (intersect >= 0) and (intersect%1 == 0):
        return "YES"
    return "NO"

print(kangaroo(0, 2, 5, 3));
