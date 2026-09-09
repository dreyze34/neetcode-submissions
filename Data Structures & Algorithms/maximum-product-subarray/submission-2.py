class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxP = [0 for i in range(n)]
        maxP[0] = max(nums[0], -float("inf"))
        minP = [0 for i in range(n)]
        minP[0] = min(nums[0], float("inf"))

        for i in range(1, n):
            maxP[i], minP[i] = max(nums[i], maxP[i-1]*nums[i], minP[i-1]*nums[i]), min(nums[i], minP[i-1]*nums[i], maxP[i-1]*nums[i])
        return max(maxP)
            