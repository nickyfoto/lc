#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#
# https://leetcode.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (53.51%)
# Total Accepted:    32.3K
# Total Submissions: 60K
# Testcase Example:  '"00110"'
#
# Give a string s, count the number of non-empty (contiguous) substrings that
# have the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively. 
# 
# Substrings that occur multiple times are counted the number of times they
# occur.
# 
# Example 1:
# 
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's
# and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of
# times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are
# not grouped together.
# 
# 
# 
# Example 2:
# 
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
# number of consecutive 1's and 0's.
# 
# 
# 
# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.
# 
#
class Solution:
    # def countBinarySubstrings(self, s: str) -> int:
    def countBinarySubstrings(self, s):
        n = len(s)
        n0 = 0
        n1 = 0
        i = 0
        res = 0
        first = s[0]
        if first == '0':
            not_first = '1'
        else:
            not_first = '0'

        while i < n:
            if s[i] == '0':
                n0 += 1
            else:
                n1 += 1
            # print('i=', i, n0, n1, 'first=', first)
            if n0 > 0 and n1 > 0 and (s[i] == first or i == n-1):
                # print('i=', i, n0, n1)
                if s[i] == first:
                    if first == '0':
                        n0 -= 1
                    else:
                        n1 -= 1
                res += min(n0, n1)
                i -= 1
                n0, n1 = 0, 0
                while s[i] != first:
                    i -= 1
                # print('i=', i)
                if first == '0':
                    first = '1'
                else:
                    first = '0'
                # first = not_first
                # break
            i += 1
            # print('reset i=', i, 'res=', res)     
        # print(i, n0, n1)
        return res


# S = Solution()
# s = '00110011'
# print(S.countBinarySubstrings(s) == 6)
# s = "10101"
# print(S.countBinarySubstrings(s) == 4)


# s = '00110' 
# print(S.countBinarySubstrings(s) == 3)

#     #0123456
# s = '1010001' # 10, 01, 10, 01
# print(S.countBinarySubstrings(s) == 4)












        
