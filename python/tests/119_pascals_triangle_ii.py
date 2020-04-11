#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (43.82%)
# Total Accepted:    212.2K
# Total Submissions: 479.3K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    def getRow(self, rowIndex):
        
        def roll(l):
            res = []
            for i in range(len(l)-1):
                res.append(l[i]+l[i+1])
            return [1]+res+[1]
        def generate(numRows):
            if numRows == 0:
                return [1]
            # t = [[1] for i in range(numRows)]
            # print(t)
            # t[0] = [1]
            t = [[1]]
            # if numRows == 0:
                # return [1]
            
            while numRows > 0:
                t.append(roll(t.pop()))
                numRows -= 1
            return t[0]
        return generate(rowIndex)
        
    def getRow(self, rowIndex):
        """
        combinatorics win
        """
        res = [1]
        for k in range(1, rowIndex + 1):
            res.append(res[-1] * (rowIndex - k + 1) // k)
        return res