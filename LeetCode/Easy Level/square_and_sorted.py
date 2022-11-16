class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr1 = []
        for i in nums:
            arr1.append(i*i)
        
        arr1 = sorted(arr1)
        return arr1