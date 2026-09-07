class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        minJump = 0
        l, r = 0, 0
        maxJump = 0
        while r < n-1:
            maxJump = max(maxJump, l + nums[l])
            if l == r:
                l = r + 1
                r = maxJump
                maxJump = 0
                minJump += 1
            else:
                l += 1
        return minJump
            