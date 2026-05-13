class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [nums[0]]
        for i in range(1, n):
            prefixSum.append(prefixSum[i-1]+nums[i])
        h = {}
        result = 0
        for j in range(n):
            if prefixSum[j] == k:
                result += 1
            if prefixSum[j] - k in h:
                result += h[prefixSum[j]-k]
            h[prefixSum[j]] = h.get(prefixSum[j], 0) + 1
        return result
        
