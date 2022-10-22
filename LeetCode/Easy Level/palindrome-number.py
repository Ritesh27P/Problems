class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        string = ''
        for i in range(len(xstr) -1, -1, -1):
            string += xstr[i]
        
        if (string == xstr):
            return True
        return False