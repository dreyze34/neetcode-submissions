class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        sortedData = sorted(zip(position, speed))
        sortedPos, sortedSpeed = zip(*sortedData)
        sortedPos, sortedSpeed = list(sortedPos), list(sortedSpeed)
        for i in range(n):
            while stack:
                curTime = (target - sortedPos[i]) / sortedSpeed[i]
                prevTime = (target - stack[-1][0]) / stack[-1][1]
                if prevTime <= curTime:
                    stack.pop()
                else:
                    break
            stack.append((sortedPos[i], sortedSpeed[i]))
        return len(stack)