class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 1:
            return strs[0]
        lowest_length = len(strs[0])
        for i in strs:
            if i == "":
                return ""
            if len(i) < lowest_length:
                lowest_length = len(i)

        word = ""
        for i in range(lowest_length):
            temp = strs[0][i]
            for j in range(0, len(strs)):
                if temp != strs[j][i]:
                    return word
            word += strs[0][i]
        
        return word