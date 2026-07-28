class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_arr = sorted(nums)
        for i in range(1, n):
            if sorted_arr[i] == sorted_arr[i-1]:
                return True
        return False