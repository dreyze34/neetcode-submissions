class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        cleaned_intervals = [intervals[0]]
        result = 0
        for i in range(1, n):
            if intervals[i][0] < cleaned_intervals[-1][1]:
                result += 1
            else:
                cleaned_intervals.append(intervals[i])
        return result