def searchInsert(nums: list[int], target: int) -> int:
    mid = len(nums)//2
    start = 0
    end = len(nums)
    while True:
        # print(start, mid, end, nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid
            mid = (start+mid)//2
        elif nums[mid] < target:
            start = mid
            mid = (mid + end)//2

print(searchInsert([1,3,5,6,9], 5))