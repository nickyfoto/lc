#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (46.30%)
# Total Accepted:    265.3K
# Total Submissions: 567.7K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],      0
# ⁠   [1,1],     1*
# ⁠  [1,2,1],    2
# ⁠ [1,3,3,1],   3*
# ⁠[1,4,6,4,1]   4
#[1,5,10,10,5,1]5 
#]
# 
# 
#
class Solution:
    # def generate(self, numRows: int) -> List[List[int]]:
    def roll(self, l):
        res = []
        for i in range(len(l)-1):
            res.append(l[i]+l[i+1])
        return [1]+res+[1]
    def generate(self, numRows):
        if numRows == 0:
            return []
        t = [[] for i in range(numRows)]
        # print(t)
        t[0] = [1]
        # print(self.roll([1,4,6,4,1]))
        # print(self.roll([1,3,3,1]))
        # print(self.roll([1,2,1]))
        # print(self.roll([1,1]))
        # print(self.roll([1]))
        for i in range(1, numRows):
            t[i] = self.roll(t[i-1])

        return t

# s = Solution()
# numRows = 5
# print(s.generate(numRows))
        
