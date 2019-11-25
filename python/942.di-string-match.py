#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#
# https://leetcode.com/problems/di-string-match/description/
#
# algorithms
# Easy (70.00%)
# Total Accepted:    29.4K
# Total Submissions: 42K
# Testcase Example:  '"IDID"'
#
# Given a string S that only contains "I" (increase) or "D" (decrease), let N =
# S.length.
# 
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ...,
# N-1:
# 
# 
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "IDID"
# Output: [0,4,1,3,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: "III"
# Output: [0,1,2,3]
# 
# 
# 
# Example 3:
# 
# 
# Input: "DDI"
# Output: [3,2,0,1]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 10000
# S only contains characters "I" or "D".
# 
#
class Solution:
    # def diStringMatch(self, S: str) -> List[int]:
    def diStringMatch(self, S):
        N = len(S)
        l = [0] * (N+1)
        for i in range(N):
            if S[i] == "I":
                if l[i+1] == 0:
                    l[i] -= 1
                elif l[i+1] > 0:
                    l[i] -= l[i+1]
                else:
                    l[i] = l[i+1] + l[i+1]
            elif S[i] == "D":
                if l[i] == 0:
                    l[i+1] -= 1
                elif l[i] > 0:
                    l[i+1] -= l[i]
                else:
                    l[i+1] = l[i] + l[i]
                # print(l)
                
        # print(l)
        order = sorted(range(len(l)), key=lambda k: l[k])
        res = list(range(N+1))

        for idx in range(N+1):
            res[order[idx]] = idx
        # print(res)
        return res

# s = Solution()

# S = "IDID"
# print(s.diStringMatch(S))


# S = "III"
# print(s.diStringMatch(S))

# S = "DDI"
# print(s.diStringMatch(S))

# S = "DD"
# print(s.diStringMatch(S))

# S = "DDD"
# print(s.diStringMatch(S))
