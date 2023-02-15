class Solution:
    def addToArrayForm(self, num, k: int):
        number = ''
        for i in num:
            number += str(i)
        
        number = int(number) + k
        return [int(i) for i in str(number)]