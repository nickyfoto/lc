#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (63.72%)
# Total Accepted:    28.1K
# Total Submissions: 44.1K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# Given two lists of closed intervals, each list of intervals is pairwise
# disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real
# numbers x with a <= x <= b.  The intersection of two closed intervals is a
# set of real numbers that is either empty, or can be represented as a closed
# interval.  For example, the intersection of [1, 3] and [2, 4] is [2,
# 3].)
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects,
# and not arrays or lists.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
# 
#
class Solution:
    # def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    def intervalIntersection(self, A, B):
        
        def check_interval(a, b):
            if a[1] < b[0] or a[0] > b[1]:
                return []
            elif a[1] == b[0]:
                return [a[1]] * 2
            elif a[0] == b[1]:
                return [a[0]] * 2
            else:
                if a[0] <= b[0] and a[1] >= b[1]:
                    return b
                elif b[0] <= a[0] and b[1] >= a[1]:
                    return a
                elif a[0] <= b[0] and a[1] >= b[0] and a[1] <= b[1]:
                    return [b[0], a[1]]
                elif a[0] >= b[0] and a[0] <= b[1] and a[1] >= b[1]:
                    return [a[0], b[1]]


        res = []
        for a in A:
            for b in B:
                interval = check_interval(a, b)
                if interval:
                    res.append(interval)
        return res

# s = Solution()
# A = [[0,2],[5,10],[13,23],[24,25]]
# B = [[1,5],[8,12],[15,24],[25,26]]
# print(s.intervalIntersection(A, B))
        
