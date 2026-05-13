class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i, j = 0, n-1
        c = 0
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
                c += 1
        return c