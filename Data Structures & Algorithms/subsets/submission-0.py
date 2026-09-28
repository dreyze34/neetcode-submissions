class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def backtrack(state, i):
            result.append(state.copy())

            if len(state) == n:
                return

            for j in range(i + 1, n):
                state.append(nums[j])
                backtrack(state, j)
                state.pop()
        
        backtrack([], -1)
        return result
