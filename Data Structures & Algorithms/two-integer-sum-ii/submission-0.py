class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        n = len(numbers)
        for i in range(n):
            diff = target - numbers[i]
            if target-diff in d:
                return [d[target-diff]+1, i+1]
            else:
                d[diff] = i
        print(d)