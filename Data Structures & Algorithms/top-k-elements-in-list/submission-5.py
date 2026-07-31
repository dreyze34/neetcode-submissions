class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        freq = {i: [] for i in range(1, n+1)}
        for key, v in h.items():
            freq[v].append(key)
        result = []
        for i in range(n, 0, -1):
            if len(freq[i]) + len(result) <= k:
                result.extend(freq[i])
        return result
