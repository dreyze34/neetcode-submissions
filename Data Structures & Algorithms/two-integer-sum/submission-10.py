class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h = {target - nums[j]: j for j in range(n)}
        for i in range(n):
            if nums[i] in h and h[nums[i]] != i:
                return [i, h[nums[i]]]
            
            
