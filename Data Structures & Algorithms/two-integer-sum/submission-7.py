class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            diff = target - nums[i]
            d[diff] = i
        for j in range(n):
            idx = d.get(nums[j], j)
            if j != idx:
                return sorted([idx, j])