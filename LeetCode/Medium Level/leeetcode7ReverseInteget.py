class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if (x >= 0):
            res = int(str(x)[::-1])
        else:
            res = int(str(abs(x))[::-1]) * -1

        if abs(res) >= 2147483648:
            return 0
        return res