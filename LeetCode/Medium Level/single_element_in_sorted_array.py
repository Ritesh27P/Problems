class Solution:
    def singleNonDuplicate(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums), 2):
            if nums[i-1] != nums[i]:
                return nums[i-1]
            

        return nums[-1]
        