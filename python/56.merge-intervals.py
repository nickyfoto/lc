#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.86%)
# Total Accepted:    424.3K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def merge(self, intervals):
        
        # res = []
        intervals.sort()
        # print(intervals)
        i = 0
        while i < len(intervals):
            int_i = intervals[i]
            j = i+1
            while j < len(intervals) and intervals[j][0] <= int_i[1]:

                # print('i=', i, 'j=', j, int_i[1], intervals[j][1], 'intervals=', intervals)
                int_i[1] = max(int_i[1], intervals[j][1])
                intervals[i] = int_i
                # print('int_i=', int_i, 'intervals[j]=', intervals[j], 'intervals=', intervals)
                intervals.remove(intervals[j])
                # print('intervals=', intervals)
            # print('out')
            i = j
        # print(intervals)
        return intervals
s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals) == [[1,6],[8,10],[15,18]])

intervals = [[1,4],[4,5]]
print(s.merge(intervals) == [[1,5]])

intervals = [[1,4],[2,3]]
print(s.merge(intervals) == [[1,4]])

intervals = [[2,3],[5,5],[2,2],[3,4],[3,4]]
print(s.merge(intervals) == [[2,4],[5,5]])





class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged










