class Solution(object):
    def twoSum(self, nums, target):
        num_hash = {}

        for i in range(len(nums)):
            choosed = target - nums[i]
            if choosed not in num_hash:
                num_hash[nums[i]] = i
            else:
                t = num_hash[choosed]
                return [t, i]
