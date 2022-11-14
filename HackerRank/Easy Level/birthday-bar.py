def birthday(s, d, m):
    # Write your code here
    choclate = 0
    for i in range(m-1, len(s)):
        temp1 = 0
        for j in range(m):
            temp1 += s[abs(i-j)]
        if temp1 == d:
            choclate += 1
    
    return choclate

