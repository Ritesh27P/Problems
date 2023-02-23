class Solution:
    def maxArea(self, height) -> int:
        if len(height) < 2:
            return 0
        if len(height) == 2:
            return min(height)
        
        high = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                temp = min(height[i], height[j]) * (j - i)
                if temp > high:
                    high = temp

        return high
