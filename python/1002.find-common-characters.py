#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (65.89%)
# Total Accepted:    25.2K
# Total Submissions: 38.2K
# Testcase Example:  '["bella","label","roller"]'
#
# Given an array A of strings made only from lowercase letters, return a list
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
# 
# 
# 
#
class Solution:
    # def commonChars(self, A: List[str]) -> List[str]:
    def commonChars(self, A):        
        d = dict([(s, A[0].count(s)) for s in set(list(A[0]))])
        for s in A[1:]:
            for k in d.keys():
                if k not in s:
                    d[k] = 0
                else:
                    if s.count(k) < d[k]:
                        d[k] = s.count(k)
        # print(d)
        res = []
        for k in d:
            res.extend([k] * d[k])
        # print(res)
        return res
            # for c in s:
                # if c not in d:
                    # del d[c]
# s = Solution()
# A = ["bella","label","roller"]
# print(s.commonChars(A))
        
# A = ["cool","lock","cook"]
# print(s.commonChars(A))