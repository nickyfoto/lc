#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (32.48%)
# Likes:    1247
# Dislikes: 144
# Total Accepted:    217.8K
# Total Submissions: 670.5K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
from bisect import bisect_left
class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    def insert(self, intervals, newInterval):
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            del intervals[i]
        intervals.insert(i, newInterval)
        return intervals

    def insert_me(self, intervals, newInterval):
        i = bisect_left(intervals, newInterval)
        intervals.insert(i, newInterval)
        # print(i, intervals)

        def merge_left(i):
            if i == 0 or intervals[i - 1][1] < intervals[i][0]:
                return i
            intervals[i - 1][1] = max(intervals[i][1], intervals[i - 1][1])
            del intervals[i]
            i -= 1
            # print('intervals=', intervals)
            return i

        def merge_right(r):
            # print('in func', r==len(intervals) - 1, intervals, r)
            if r == len(intervals) - 1 or intervals[r][1] < intervals[r + 1][0]:
                return
            # print('here', intervals)
            while r + 1 < len(intervals) and intervals[r][1] >= intervals[r + 1][0]:
                intervals[r][1] = max(intervals[r + 1][1], intervals[r][1])
                del intervals[r + 1]
        if i > 0:
            # print('i=', i)
            r = merge_left(i)
            # print('r=', r, intervals, r == len(intervals) - 1)
            merge_right(r)
        else:
            merge_right(i)
        return intervals
# @lc code=end
