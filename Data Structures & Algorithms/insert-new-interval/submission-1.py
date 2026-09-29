class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        for i in range(n):
            if intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        result.append(newInterval)
        return result
