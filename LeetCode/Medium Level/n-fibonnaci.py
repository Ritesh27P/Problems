class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        arr = [0, 1, 1]
        for i in range(2, n):
            arr.append(sum(arr))
            arr.pop(0)

        return arr[-1]
        