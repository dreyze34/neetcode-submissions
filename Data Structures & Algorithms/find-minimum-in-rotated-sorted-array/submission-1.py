class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = 0, n-1
        m = float("inf")
        while a <= b:
            c = (a+b)//2
            if nums[c] > nums[b]:
                a = c + 1
            else:
                b = c - 1
            m = min(m, nums[c])
        return m