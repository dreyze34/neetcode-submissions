class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for j in range(n):
            curTemp = temperatures[j]
            while stack and curTemp > temperatures[stack[-1]]:
                i = stack.pop()
                diff = j - i
                result[i] = diff
            stack.append(j)
        return result

                
            
                