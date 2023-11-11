class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        res = 0
        while r <= len(s):
            set1 = len(set(s[l:r+1]))
            if set1 == len(s[l:r+1]):
                res = max(set1, res)
                r += 1
            else:
                l += 1
                r += 1

        return res

