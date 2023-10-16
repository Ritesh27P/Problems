class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0

        p1 = 0
        p2 = len(height) -1

        while p1 < p2:
            minValue = min(height[p1], height[p2])
            if (minValue*(p2-p1) > res):
                res = minValue*(p2-p1)
            
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1

        return res