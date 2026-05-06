class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max = 0
        for i in range(len(nums)):
            num = nums[i]
            j = 1
            if num-1 not in s:
                while num+j in s:
                    j += 1
                if j > max:
                    max = j
        return max

                
        
            
