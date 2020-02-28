#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (44.87%)
# Likes:    173
# Dislikes: 34
# Total Accepted:    12K
# Total Submissions: 26.6K
# Testcase Example:  '["un","iq","ue"]'
#
# Given an array of strings arr. String s is a concatenation of a sub-sequence
# of arr which have unique characters.
# 
# Return the maximum possible length of s.
# 
# 
# Example 1:
# 
# 
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and
# "ique".
# Maximum length is 4.
# 
# 
# Example 2:
# 
# 
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# 
# 
# Example 3:
# 
# 
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.
# 
# 
#

# @lc code=start
class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    def maxLength(self, arr):
        """
        @lee215
        if word contains duplicate letter, continue
        for each c in dp:
            if this c has common intersection with a:
                continue
            dp.append(a union c)
        return max length
        """
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for c in dp[:]:
                if a & c:
                    continue
                dp.append(a | c)
        return max(map(len, dp))
# @lc code=end
