def delete_and_eran(nums):
    value = 0
    nums = nums
    while len(nums) > 0:
        print(nums)
        # nums.remove(max(nums))
        if (max(nums)-1) in nums:
            print('exists ', max(nums)-1)
        nums.remove(max(nums))

    return value

print(delete_and_eran([2, 2, 3, 3, 3, 4]))