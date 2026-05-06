class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            d[nums[i]] = d.get(nums[i], 0)+1
        l = sorted(d.keys(), key=d.get)
        return l[-k:]
        
