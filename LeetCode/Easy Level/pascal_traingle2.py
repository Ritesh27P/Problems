class Solution:
    def getRow(self, rowIndex: int):
        arr = [1, 3, 3, 1]
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        if rowIndex == 2:
            return [1, 2, 1]
        
        for i in range(3, rowIndex):
            temp = [1]
            for j in range(1, len(arr)):
                temp.append(arr[j-1] + arr[j])
            temp.append(1)
            print(temp)
            arr = temp

        return arr