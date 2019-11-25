#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (45.32%)
# Total Accepted:    53.7K
# Total Submissions: 118.3K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
# 
# You need to return whether the student could be rewarded according to his
# attendance record.
# 
# Example 1:
# 
# Input: "PPALLP"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "PPALLL"
# Output: False
# 
# 
# 
# 
# 
#
class Solution:
    def checkRecord(self, s: str) -> bool:
        n_A = 0
        # n_L = 0
        n = len(s)
        for i in range(n):
        	if s[i] == 'A':
        		n_A += 1
        		if n_A > 1:
        			return False
        	if s[i] == 'L':
        		if i < n-2 and s[i+1] == 'L' and s[i+2] == 'L':
        			return False
        return True
# S = Solution()
# s = 'LALL'
# print(S.checkRecord(s))