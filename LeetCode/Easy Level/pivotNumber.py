def pivotIndex(nums):
    S = sum(nums)
    lsum = 0
    for i, x in enumerate(nums):
        if (S - lsum -x) == lsum:
            return i
        else:
            lsum += x
        
    return -1



print(pivotIndex([1,7,3,6,5,6]))
print()
print(pivotIndex([1,2,3]))
print()
print(pivotIndex([2,1,-1]))
print()
print(pivotIndex([-1,-1,-1,-1,-1,-1]))