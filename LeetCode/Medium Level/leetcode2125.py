class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = []
        res = 0

        for i in bank:
            if i.count("1"):
                arr.append(i.count("1"))
        
        if len(arr) < 2:
            return 0

        for i in range(1, len(arr)):
            res += arr[i]*arr[i-1]
        
        return res