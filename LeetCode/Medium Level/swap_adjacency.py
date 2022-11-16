def canTransform(start, end):
    temp = ''
    for i in range(1, len(start), 2):
        temp += start[i]
        temp += start[i-1]

    print(temp)

canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX")
