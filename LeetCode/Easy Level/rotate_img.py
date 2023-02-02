class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix)-1, -1, -1):
                temp.append(matrix[j][i])
            print(temp)
            new_matrix.append(temp)
        
        for i in range(len(matrix)):
            matrix[i] = new_matrix[i]
                
