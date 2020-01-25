#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (34.46%)
# Likes:    1353
# Dislikes: 4001
# Total Accepted:    401.7K
# Total Submissions: 1.2M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s

        d = defaultdict(list)
        n_zz = numRows - 2
        i = 0
        while i < n:
            row = 0
            while i < n and row < numRows:
                # print("i=", i, "row=", row)
                d[row].append(s[i])
                row += 1
                i += 1

            row = n_zz
            while i < n and row > 0:
                # print('here i=', i, 'row=', row)
                d[row].append(s[i])
                row -= 1
                i += 1
            
                
        # print(d)
        res = []
        for k in d:
            res.extend(d[k])
        return "".join(res)
        
# @lc code=end
