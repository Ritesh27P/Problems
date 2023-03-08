class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        pointer = 0
        value = 0
        while pointer < k:
            value += 1
            if value not in arr:
                pointer += 1
             
        
        return value