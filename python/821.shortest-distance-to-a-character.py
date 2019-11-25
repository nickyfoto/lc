#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
# https://leetcode.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (64.43%)
# Total Accepted:    46K
# Total Submissions: 71.4K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.
# 
# Example 1:
# 
# 
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 
# 
# Note:
# 
# 
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
# 
# 
#
class Solution:
    # def shortestToChar(self, S: str, C: str) -> List[int]:
    def shortestToChar(self, S: str, C: str):
        n = len(S)
        L = [0] * n


        def update(i):
            if S[i] == C:
                return
            else:
                if L[i] != 0:
                    return
                else:
                    if i == 0:
                        L[i] = S.index(C)
                    else:
                        if L[i-1] != 0:
                            # print(i-1+L[i-1], )
                            if i - 1 + L[i-1] < n and S[i - 1 + L[i-1]] == C:
                                L[i] = L[i-1] - 1
                            elif i - 1 - L[i-1] >= 0 and S[i - 1 - L[i-1]] == C:
                                # print(i, S[i],S[i+1: i+1+L[i-1]])
                                right = S[i+1: i+1+L[i-1]]
                                if C not in right:
                                    L[i] = L[i-1] + 1
                                else:
                                    L[i] = right.index(C) + 1
                            else:
                                print(L, i)
                                todo
                        else:
                            L[i] = 1

        for i in range(n):
            update(i)
        return L 


s = Solution()
S = "loveleetcode"
C = 'e'
print(s.shortestToChar(S, C))