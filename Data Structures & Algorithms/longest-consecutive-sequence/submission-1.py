class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        maxSeq = 0
        for i in range(n):
            if nums[i]-1 not in s:
                curSeq = 1
                while True:
                    if nums[i]+curSeq in s:
                        curSeq += 1
                    else:
                        break
                maxSeq = max(maxSeq, curSeq)
        return maxSeq
                    


