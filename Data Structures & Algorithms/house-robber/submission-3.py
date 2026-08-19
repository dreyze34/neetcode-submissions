class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [nums[0], max(nums[:2])]
        for i in range(2, n):
            dp.append(max(dp[i-1], dp[i-2]+nums[i]))
        return dp[-1]