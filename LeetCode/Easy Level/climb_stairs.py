def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    
    arr = [1, 1]
    for i in range(1, n):
        arr[0], arr[1] = arr[1], sum(arr)
    return arr[-1]