from typing import List


class Solution1:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0

        for h in nums:
            op1 = prev2 + h
            op2 = prev1
            robbed = max(op1, op2)
            prev2 = prev1
            prev1 = robbed
        return robbed


class Solution:
    def rob(self, nums: List[int]) -> int:
        s = Solution1()
        circle_length = len(nums)
        op1 = nums[0] + s.rob(nums[2:circle_length-1])
        op2 = s.rob(nums[1:circle_length])
        return max(op1, op2)



# a = Solution().rob([1, 2, 3, 1]) [2,1,1,2]
# a = Solution1().rob([2,1,1,2])
# print(a)

# odd = nums[0::2]
#         even = nums[1::2]
#
#         o = sum(odd)
#         e = sum(even)
#         if e > o:
#             return e
#         else:
#             return o