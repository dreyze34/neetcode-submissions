class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        if k == 0:
            return False
        s = set()
        s.add(nums[0])
        for j in range(1, n):
            while abs(i-j) > k:
                s.remove(nums[i])
                i += 1
            if nums[j] in s:
                return True
            s.add(nums[j])
        return False