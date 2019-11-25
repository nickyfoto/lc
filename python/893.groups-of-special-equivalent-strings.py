#
# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#
# https://leetcode.com/problems/groups-of-special-equivalent-strings/description/
#
# algorithms
# Easy (62.75%)
# Total Accepted:    15.7K
# Total Submissions: 25K
# Testcase Example:  '["abcd","cdab","cbad","xyzz","zzxy","zzyx"]'
#
# You are given an array A of strings.
# 
# Two strings S and T are special-equivalent if after any number of moves, S ==
# T.
# 
# A move consists of choosing two indices i and j with i % 2 == j % 2, and
# swapping S[i] with S[j].
# 
# Now, a group of special-equivalent strings from A is a non-empty subset S of
# A such that any string not in S is not special-equivalent with any string in
# S.
# 
# Return the number of groups of special-equivalent strings from A.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a","b","c","a","c","c"]
# Output: 3
# Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["aa","bb","ab","ba"]
# Output: 4
# Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
# 
# 
# 
# Example 3:
# 
# 
# Input: ["abc","acb","bac","bca","cab","cba"]
# Output: 3
# Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
# 
# 
# 
# Example 4:
# 
# 
# Input: ["abcd","cdab","adcb","cbad"]
# Output: 1
# Explanation: 1 group ["abcd","cdab","adcb","cbad"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 1000
# 1 <= A[i].length <= 20
# All A[i] have the same length.
# All A[i] consist of only lowercase letters.
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def numSpecialEquivGroups(self, A: List[str]) -> int:
    def numSpecialEquivGroups(self, A):
        # n = len(A[0])
        # if n < 3:
        #     return len(set(A))
        def all_alternates(s):
            # input string
            # output list of alternatives
            n = len(s)
            even = sorted([s[i] for i in range(len(s)) if i % 2 == 0])
            odd = sorted([s[i] for i in range(len(s)) if i % 2 == 1])
            return tuple(even + odd)
        # print([A[0][i] for i in range(len(A[0])) if i % 2 == 0])
        # print([A[0][i] for i in range(len(A[0])) if i % 2 == 1])
        # print(all_alternates(A[0]))
        # groups = [all_alternates(A[0])]
        # for i in range(1, n):
        #     for g in groups:
        #         if all_alternates(A[i])
        # print(list(map(all_alternates, A)))
        # print(set(map(all_alternates, A)))
        # print(set)
        return len(set(map(all_alternates, A)))



# s = Solution()
# A = ["a","b","c","a","c","c"]
# print(s.numSpecialEquivGroups(A))
# A = ["aa","bb","ab","ba"]
# print(s.numSpecialEquivGroups(A))
# A = ["abc","acb","bac","bca","cab","cba"]
# print(s.numSpecialEquivGroups(A))
# A = ["abcd","cdab","adcb","cbad"]
# print(s.numSpecialEquivGroups(A))
