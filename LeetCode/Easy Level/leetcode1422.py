class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = str(s)
        res = 0
        for i in range(1, len(s)):
            if s[:i].count("0") + s[i:].count('1') > res:
                res = s[:i].count("0") + s[i:].count('1')
    
        return res
        