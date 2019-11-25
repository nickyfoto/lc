#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (57.04%)
# Total Accepted:    105K
# Total Submissions: 184.1K
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
# 
# Example 1:
# 
# Input:
# "tree"
# 
# Output:
# "eert"
# 
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
# 
# 
# 
# Example 2:
# 
# Input:
# "cccaaa"
# 
# Output:
# "cccaaa"
# 
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# 
# 
# 
# Example 3:
# 
# Input:
# "Aabb"
# 
# Output:
# "bbAa"
# 
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# 
# 
#
from collections import Counter
# from operator import itemgetter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        l = list(s)
        l = [(x, c[x], ord(x)) for x in l]
        # print(l)
        # l = sorted(l, key=itemgetter(1,2), reverse=True)
        l = sorted(l, key=lambda x: [x[1], x[2]], reverse=True)
        # print(l)
        return "".join([s[0] for s in l])


# S = Solution()
# s = "tree"
# print(S.frequencySort(s))

# s = "cccaaa"
# print(S.frequencySort(s))


# s = "loveleetcode"
# print(S.frequencySort(s))
# "eeeelolovtcd"
# "eeeeoollvtdc"



















