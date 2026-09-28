class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        s = 0
        min_lenght = float("inf")
        for r in range(n):
            s += nums[r]
            while s >= target:
                min_lenght = min(min_lenght, r - l + 1)
                s -= nums[l]
                l += 1
                
        return min_lenght if min_lenght != float("inf") else 0
