def utopianTree(n):
    # Write your code here
    if n == 0:
        return 1
    if n == 1:
        return 2
    height = 2
    for i in range(2, n+1):
        if i%2 == 0:
            height += 1
        else:
            height *= 2
    
    return height



print(utopianTree(2))
print(utopianTree(4))

## my solution till
