class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        value = 0
        
        i = 0
        while True:
            if (i == len(s)): return value
            if (i+1 != len(s) and (data[str(s[i+1])] > data[str(s[i])])):
                value += (data[str(s[i+1])] - data[str(s[i])])
                i += 2
                continue
            else:
                value += data[str(s[i])]
                i += 1
        return value