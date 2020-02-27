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
from collections import Counter, defaultdict
from pprint import pprint
class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    def maxLength(self, arr):
        new_arr = []
        for a in arr:
            if len(Counter(a)) == len(a):
                new_arr.append(a)
        if not new_arr:
            return 0
        self.mx = 0
        def backtrack(arr, temp):
            if not arr:
                return
            else:
                for i in range(len(arr)):
                    s = set(arr[i])
                    if temp & s:
                        continue
                    temp |= s
                    self.mx = max(self.mx, len(temp))
                    backtrack(arr[i + 1:], temp)
                    temp -= s

                    
        backtrack(new_arr, set())
        return self.mx
# @lc code=end
