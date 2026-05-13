class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        h = {}
        result = []
        for i in range(n):
            h[nums[i]] = h.get(nums[i], 0) + 1
            if h[nums[i]] == int(n/3)+1:
                result.append(nums[i])
        return result