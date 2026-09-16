class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if abs(nums[0]) == abs(target) else 0
        totalSum = sum(nums)        
        sums = [0 for _ in range(2 * totalSum + 1)]
        sums[totalSum + nums[0]] += 1
        sums[totalSum - nums[0]] += 1
        for i in range(1, n):
            arr = [0 for _ in range(2 * totalSum + 1)]
            for j in range(len(sums)):
                if j - nums[i] >= 0:
                    arr[j - nums[i]] += sums[j]
                if j + nums[i] < len(sums):
                    arr[j + nums[i]] += sums[j]
            sums = arr
        return sums[totalSum + target] if abs(target) <= totalSum else 0
