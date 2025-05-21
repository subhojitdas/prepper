from dill import pointers


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        len1 = len(nums1) # A => shorter length
        len2 = len(nums2) # B => larger length
        total_len = (len1 + len2)
        half = total_len // 2 # 0 1 2 3 4 5 6 7 8 9 10

        l = 0
        r = len(nums1) - 1
        while True:
            take1 = (l + r) // 2
            take2 = half - take1 - 2

            Aleft = nums1[take1] if take1 >= 0 else float('-inf')
            Aright = nums1[take1 + 1] if (take1 + 1) < len1 else float('inf')
            Bleft = nums2[take2] if take2 >=0 else float('-inf')
            Bright = nums2[take2 + 1] if (take2 + 1) < len2 else float('inf')

            if Aleft <= Bright and Aright >= Bleft:
                if total_len % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = take1 - 1
            else:
                l = take1 + 1


a = Solution().findMedianSortedArrays([1,2], [3,4])
print(a)

