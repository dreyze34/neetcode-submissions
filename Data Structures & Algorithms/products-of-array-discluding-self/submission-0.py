class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = [1], [1]
        for i in range(1, n):
            pre.append(pre[i-1]*nums[i-1])
            suf.append(suf[i-1]*nums[n-i])
        res = [pre[i]*suf[n-i-1] for i in range(n)]
        return res