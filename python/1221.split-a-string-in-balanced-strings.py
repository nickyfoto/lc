#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#
# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
#
# algorithms
# Easy (80.38%)
# Total Accepted:    7.7K
# Total Submissions: 9.5K
# Testcase Example:  '"RLRRLLRLRL"'
#
# Balanced strings are those who have equal quantity of 'L' and 'R'
# characters.
# 
# Given a balanced string s split it in the maximum amount of balanced
# strings.
# 
# Return the maximum amount of splitted balanced strings.
# 
# 
# Example 1:
# 
# 
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring
# contains same number of 'L' and 'R'.
# 
# 
# Example 2:
# 
# 
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring
# contains same number of 'L' and 'R'.
# 
# 
# Example 3:
# 
# 
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'
# 
# 
#
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        

        n = len(s)

        i = 0
        res = 0
        while i < n:
            a = s[i]
            j = i+1
            ca = 1 #count a
            cb = 0
            while j < n and ca != cb:
                if s[j] == a:
                    ca += 1
                elif s[j] != a:
                    cb += 1
                j += 1
            res += 1
            i = j
        # print(res)

        return res



S = Solution()
s = "RLRRLLRLRL"
print(S.balancedStringSplit(s) == 4)

s = "RLLLLRRRLR"
print(S.balancedStringSplit(s) == 3)


s = "LLLLRRRR"
print(S.balancedStringSplit(s) == 1)










