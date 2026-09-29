class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        result = 0
        for i in range(1, n):
            if intervals[i][0] < last_end:
                result += 1
            else:
                last_end = intervals[i][1]
        return result