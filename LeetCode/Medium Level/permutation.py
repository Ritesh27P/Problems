def permutate(nums):
    result = []
    if len(nums) == 1:
        return [nums[:]]
    
    temp1 = nums
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutate(nums)
        # print(perms)
        for perm in perms:
            perm.append(n)
        
        for i in perms:
            print(i)
            result.append(i)
        nums.append(n)
    
    return result


print(permutate([1, 2, 3]))