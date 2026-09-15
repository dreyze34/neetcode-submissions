class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        while start < n:
            tank = 0
            for j in range(n):
                idx = (start + j) % n
                tank += gas[idx]
                if tank < cost[idx]:
                    start += j + 1
                    break
                else:
                    if j == n-1:
                        return start
                    tank -= cost[idx]
        return -1