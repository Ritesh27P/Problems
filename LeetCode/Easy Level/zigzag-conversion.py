def conversion(s, numRows):
    arr = []
    zigzag = ''
    numRows = numRows + (numRows//2)
    while (len(arr) >= 0):
        for i in range(0, len(arr), numRows):
            print(arr[i])
            zigzag += arr[i]
            arr.pop(i)