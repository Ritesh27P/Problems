class Solution:
    def generate(self, numRows: int):
        arr = [[1], [1, 1], [1, 2, 1]]
        
        if numRows == 1:
            return arr[:1]
        if numRows == 2:
            return arr[:2]
        if numRows == 3:
            return arr[:3]
        
        for i in range(3, numRows):
            temp = [1]
            for j in range(1, len(arr[-1])):
                temp.append(arr[-1][j-1] + arr[-1][j])
            temp.append(1)

            arr.append(temp)

        return arr
