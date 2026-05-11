class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        a, b = 0, n-1
        if target == nums[a]:
            return a
        elif target == nums[b]:
            return b
        while b-a > 1:
            c = a + int((b-a)/2)
            if nums[c] == target:
                return c
            elif target < nums[c]:
                b = c
            else:
                a = c
        return -1

        