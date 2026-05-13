class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        h = {}
        for i in range(n):
            h[nums[i]] = h.get(nums[i], 0) + 1
            if h[nums[i]] > int(n/2):
                return nums[i]
        