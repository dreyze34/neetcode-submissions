class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        first = [0]*(n-1)
        last = [0]*(n-1)
        first[0], first[1] = nums[0], max(nums[:2])
        last[0], last[1] = nums[1], max(nums[1:3])
        for i in range(2, n-1):
            first[i] = max(first[i-2]+nums[i], first[i-1])
            last[i] = max(last[i-2]+nums[i+1], last[i-1])
        return max(first[-1], last[-1])

