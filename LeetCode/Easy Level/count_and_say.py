class Solution:
    def calculate(self, s: str):
        lst = []
        temp = 0

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                continue
            else:
                lst.append(s[temp:i])
                temp = i
        lst.append(s[temp:])
        
        s = ""
        for i in lst:
            s += str(len(i)) + i[0]
        return s      

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"

        lst = ["11"]

        for i in range(2, n):
            lst.append(self.calculate(lst[-1]))

        return lst[-1]

