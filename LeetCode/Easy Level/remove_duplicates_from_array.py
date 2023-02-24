class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) < 2:
            return
        
        pointer = 1
        while pointer < len(nums):
            if nums[pointer] in nums[0:pointer]:
                nums.pop(pointer)
            else:
                pointer += 1


        


            
        

        