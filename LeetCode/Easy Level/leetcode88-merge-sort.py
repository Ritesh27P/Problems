class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p1, p2, p = m-1, n-1, m+n-1

        while p1 >= 0 and p2 >= 0:
            print(p1, p2, p)
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                nums1[p1] = 0
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


        




