class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        total_len = (len1 + len2)
        required_len = total_len / 2

        ptr1 = 0
        ptr2 = 0
        for i in range(required_len):
            if nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1
