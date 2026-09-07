class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        target = n - 1
        minJump = 0
        i = 0
        while target != 0:
            if i + nums[i] >= target:
                minJump += 1
                target = i
                i = 0
            else:
                i += 1
        return minJump
        