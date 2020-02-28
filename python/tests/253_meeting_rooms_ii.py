#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (44.70%)
# Likes:    2183
# Dislikes: 31
# Total Accepted:    241.8K
# Total Submissions: 541.1K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
from heapq import heappush, heappop
class Solution:
    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    def minMeetingRooms(self, intervals):
        """
        sort intervals by start time
        push first meeting's end time to pq
        iterate the rest meetings
        if top of pq (earlist end time) <= curr meeting start
            pop this meeting, add curr meeting end time
        directly add current meeting
        """
        if not intervals:
            return 0
        free_rooms = []
        intervals.sort(key = lambda x: x[0])
        heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heappop(free_rooms)
            heappush(free_rooms, i[1])
        return len(free_rooms)
        
# @lc code=end
