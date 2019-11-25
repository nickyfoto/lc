#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.16%)
# Total Accepted:    284.7K
# Total Submissions: 565.9K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#
class Solution:
    # def firstUniqChar(self, s: str) -> int:
    def firstUniqChar(self, s):
        l = list(set(list(s)))
        d = dict(zip([x for x in l], [s.count(x) for x in l]))
        # print(d)
        n = len(s)
        for i in range(n):
            if d[s[i]] == 1:
                return i
        return -1
        
# S = Solution()
# s = "leetcode"
# print(S.firstUniqChar(s))

# s = "loveleetcode"
# print(S.firstUniqChar(s))
