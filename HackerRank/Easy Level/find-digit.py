def findDigits(n):
    # Write your code here
    value = 0
    number = str(n)
    for i in number:
        if int(i) == 0:
            continue
        elif n%int(i) == 0:
            value += 1
            
    return value