class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:
            if (target >= i[0]) and (target <= i[len(i)-1]):
                if target in i:
                    return True
                return False
        
        return False