class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = {i: 0 for i in range(1, n+1)}
        is_trusted = {i: 0 for i in range(1, n+1)}
        for a, b in trust:
            trusting[a] += 1
            is_trusted[b] += 1
        
        for k in trusting:
            if trusting[k] == 0 and is_trusted[k] == n - 1:
                return k
        return -1
