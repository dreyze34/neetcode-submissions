class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        maxP = nums[0]
        minP = nums[0]
        for i in range(1, n):
            maxP, minP = max(nums[i], maxP*nums[i], minP*nums[i]), min(nums[i], minP*nums[i], maxP*nums[i])
            res = max(res, maxP)
        return res