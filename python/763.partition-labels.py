#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (71.78%)
# Total Accepted:    61.4K
# Total Submissions: 85.5K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
# 
# 
# Example 1:
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# 
#
class Solution:
    # def partitionLabels(self, S: str) -> List[int]:
    def partitionLabels(self, S):
        n = len(S)
        res = []
        unique = []
        i = 0
        c = 0
        while i < n:
            if S[i] not in unique:
                unique.append(S[i])
                c += 1
            if i < n - 1:
                i += 1
            # print(unique, S[i], 'c =', c)
            if S[i] in unique:
                c += 1
            else:
                # print('i = ', i, 'S[i] = ', S[i], list(range(i+1, n)), 'c =', c)
                for cc in range(i+1, n):
                    if S[cc] in unique:
                        # print('cc =', cc, 'S[cc] = ', S[cc])
                        unique.append(S[i])
                        c += 1
                        break
                    if cc == n - 1:
                        # print('here')
                        res.append(c)
                        # print('res =', res)
                        c = 0
                        unique = []
            # print('i =', i, 'unique=', unique, 'c =', c, 'cc =', cc, 'n =', n, 'S[cc] = ', S[cc])
            if i == n - 1:
                res.append(c)
                if S[i] not in unique:
                    res.append(1)
                return res
# s = Solution()
# S = "ababcbacadefegdehijhklij"
# print(s.partitionLabels(S) == [9,7,8])


# S = "eaaaabaaec"
# print(s.partitionLabels(S) == [9, 1])