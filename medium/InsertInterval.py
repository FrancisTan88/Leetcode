from typing import List


class Solution:
    """
    time: O(n^2), given n is the length of the intervals
    space: O(1)
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(interval1, interval2):
            if (interval1[0] >= interval2[0] and interval1[0] <= interval2[1]) \
                    or (interval2[0] >= interval1[0] and interval2[0] <= interval1[1]):
                return True
            return False

        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        intervals.append(newInterval)
        idx = len(intervals) - 1
        while idx > 0:
            if overlap(intervals[idx], intervals[idx-1]):
                intervals[idx] = merge(intervals[idx], intervals[idx-1])
                intervals.pop(idx-1)
            elif intervals[idx][0] < intervals[idx-1][0]:
                tmp = intervals[idx]
                intervals[idx] = intervals[idx-1]
                intervals[idx-1] = tmp
            idx -= 1
        return intervals

    """
    time: O(n), given n is the length of the intervals
    space: O(n), the cost of "ans"
    """

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        idx = 0
        n = len(intervals)
        while idx < n and intervals[idx][1] < newInterval[0]:
            ans.append(intervals[idx])
            idx += 1
        while idx < n and newInterval[1] >= intervals[idx][0]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        ans.append(newInterval)
        while idx < n:
            ans.append(intervals[idx])
            idx += 1
        return ans
