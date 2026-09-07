class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("inf")
        j = 0
        n = len(nums)
        s = 0
        while j < n:
            s += nums[j]
            if s > maxSum:
                maxSum = s
            if s < 0:
                s = 0
            j += 1
        return maxSum