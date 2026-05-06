class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {val: i for i, val in enumerate(nums)}
        for i in range(n):
            difference = target - nums[i]
            if difference in d:
                j = d[difference]
                if j != i:
                    return [i, d[difference]]
            
        