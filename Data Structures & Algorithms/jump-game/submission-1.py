class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        i, target = n-2, n-1
        while i >= 0:
            if nums[i] >= target-i:
                target = i
            i -= 1
        return target == 0