def connectingTowns(n, routes):
    value = 1
    for i in routes:
        value *= i
    return value%1234567