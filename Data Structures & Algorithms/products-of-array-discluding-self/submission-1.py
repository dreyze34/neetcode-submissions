class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, sub = [1]*n, [1]*n
        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i-1]
            sub[-i-1] = nums[-i] * sub[-i]
        result = [pre[i]*sub[i] for i in range(n)]
        return result