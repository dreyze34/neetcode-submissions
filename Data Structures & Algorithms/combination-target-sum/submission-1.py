from collections import Counter

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        def backtrack(state, state_sum, j):
            if state_sum == target:
                result.append(state.copy())
                return
            elif state_sum < target:
                for i in range(j, n):
                    state.append(nums[i])
                    state_sum += nums[i]
                    backtrack(state, state_sum, i)
                    state.pop()
                    state_sum -= nums[i]
        
        backtrack([], 0, 0)
        return result