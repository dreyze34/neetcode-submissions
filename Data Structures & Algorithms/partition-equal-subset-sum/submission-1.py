import heapq

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        n = len(nums)
        target = totalSum // 2
        dp = [False for _ in range(target+ 1)]
        dp[0] = True
        for i in range(n):
            for j in range(target, -1, -1):
                if dp[j] and j + nums[i] <= target:
                    dp[j + nums[i]] = True
        return dp[-1]
                
            
                
