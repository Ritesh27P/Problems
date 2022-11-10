def beautifulDays(i, j, k):
    # Write your code here
    beautifulDay = 0
    print(i, j, k)
    for iter in range(i, j+1):
        str1 = str(iter)
        reverse_int = str1[::-1]
        
        day = abs((iter - int(reverse_int))/k)
        if day.is_integer():
            beautifulDay += 1
            print('hi')
    return beautifulDay
        