class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        if n < 7:
            for i in range(0, n):
                res += i+1
            return res
        
        arr = [1,2,3,4,5,6,7]
        for i in range(n//7):
            res += sum(arr)
            arr.pop(0)
            arr.append(arr[-1]+1)
        
        temp = n//7 + 1
        for i in range(arr[0], n%7+arr[0]):
            res += i

        return res


        
        