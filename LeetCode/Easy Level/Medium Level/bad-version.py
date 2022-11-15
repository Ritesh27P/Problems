class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid = n//2
        start = 0
        end = n
        if isBadVersion(n) == True:
            if isBadVersion(n-1) == False:
                return n
        while True:
            print(mid, start, end, n)
            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) == False:
                    return mid
                end = mid
                mid = (start + mid)//2
                # end = mid
            else:
                start = mid
                mid = (mid + end)//2