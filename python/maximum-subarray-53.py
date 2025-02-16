###
# 53.Maximum Subarray
# Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
###

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # nums = [4, -2, 3, 1, 5, -13, 2]
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum
