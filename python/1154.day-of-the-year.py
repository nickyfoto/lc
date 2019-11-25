#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#
# https://leetcode.com/problems/day-of-the-year/description/
#
# algorithms
# Easy (49.58%)
# Total Accepted:    7.4K
# Total Submissions: 15K
# Testcase Example:  '"2019-01-09"\r'
#
# Given a string date representing a Gregorian calendar date formatted as
# YYYY-MM-DD, return the day number of the year.
# 
# 
# Example 1:
# 
# 
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# 
# 
# Example 2:
# 
# 
# Input: date = "2019-02-10"
# Output: 41
# 
# 
# Example 3:
# 
# 
# Input: date = "2003-03-01"
# Output: 60
# 
# 
# Example 4:
# 
# 
# Input: date = "2004-03-01"
# Output: 61
# 
# 
# 
# Constraints:
# 
# 
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
# 
#
from calendar import monthrange
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, (date.split('-')))
        # print(y, m, d)
        # days = []
        
        days = 0
        for i in range(1, m):
            days += monthrange(y, i)[1]
        days += d
        return days

# s = Solution()
# date = "2019-01-09"
# date = "2019-02-10"
# date = "2003-03-01"
# print(s.dayOfYear(date))
