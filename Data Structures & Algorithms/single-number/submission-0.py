class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        n = len(nums)
        for i in range(n):
            h[nums[i]] = h.get(nums[i], 0) + 1
            if h[nums[i]] == 2:
                h.pop(nums[i])
        return list(h.keys())[-1]