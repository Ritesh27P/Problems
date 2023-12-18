
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min(nums)
        nums.remove(min1)

        max1 = max(nums)
        nums.remove(max1)

        return ((max1* max(nums)) - (min1 * min(nums)))