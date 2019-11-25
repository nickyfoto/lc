#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.33%)
# Total Accepted:    447.3K
# Total Submissions: 1.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs):
        # print(strs)
        # print(list(map(len, strs)))
        if not strs:
            return ""
        min_length = min(list(map(len, strs)))
        # print(min_length)
        res = ""
        if min_length > 0:
            for i in range(min_length):
                l = [st[i] for st in strs]
                if len(set(l))== 1:
                    res += l[0]
                else:
                    return res
        # print(res)
        return res



# s = Solution()
# a = ["flower","flow","flight"]
# a = ["dog","racecar","car"]
# a = ["aca","cba"]
# s.longestCommonPrefix(a)