class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = []
        def backtrack(prev_xor, i):
            if i == n:
                return
            
            if i >= 0:
                new_xor = prev_xor ^ nums[i]
                result.append(new_xor)
            else:
                new_xor = 0

            for j in range(i+1, n):
                backtrack(new_xor, j)
        
        backtrack(0, -1)
        return sum(result)
