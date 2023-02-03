class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                string += i
        
        if string == string[::-1]:
            return True
        return False