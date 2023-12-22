class Solution:
    def threeSum(self, nums):
        num1 = sorted(nums)
        print(num1)
        res = []
        l, r = 0, len(num1) - 1
        while r > l:
            if num1[l] + num1[r] >= 0:
                j = l + 1
            else:
                j = r - 1
            
            print(l, r, j, num1[l], num1[r], num1[j])

            if num1[l] + num1[r] + num1[j] == 0:
                res.append([num1[l], num1[r], num1[j]])
                l += 1
            elif num1[l] + num1[r] + num1[j] < 0:
                l += 1
            else:
                r -= 1

        return res

s1 = Solution()
print(s1.threeSum([-1,0,1,2,-1,-4]))