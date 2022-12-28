# Brute forse method #
def arrayManipulation(n, queries):
    # Write your code here
    x = [0 for _ in range(n)]
    
    for i in queries:
        for j in range(i[0]-1, i[1]):
            x[j] += i[2]
        
    return max(x)

