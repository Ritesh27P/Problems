def birthday(s, d, m):
    # Write your code here
    get_cocholate = 0
    for i in range(0, (len(s) - m)):
        sum = 0
        for j in range(m):
            sum += s[i+j]
            # print(sum)
        if (sum == d):
            get_cocholate += 1;
    
    return get_cocholate

birthday([1, 2, 1, 3, 2], 3, 2);
print(birthday([1, 2, 1, 3, 2], 3, 2))

