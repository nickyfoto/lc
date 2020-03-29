#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (57.54%)
# Total Accepted:    10.3K
# Total Submissions: 17.9K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters(can be none) deleted without changing the relative order
# of the remaining characters. (eg, "ace" is a subsequence of "abcde" while
# "aec" is not). A common subsequence of two strings is a subsequence that is
# common to both strings.
# 
# 
# 
# If there is no common subsequence, return 0.
# 
# 
# Example 1:
# 
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.
# 
# 
#
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # print('lcs')
        # if text1 == text2:
            # return len(text1)
        L = [[x]*len(text2) for x in [0]*len(text1)]
        # print(L)
        for i in range(len(L)):
            for j in range(len(L[0])):
                # print(i, j)
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        L[i][j] = 1
                    else:
                        L[i][j] = 1 + L[i-1][j-1]
                else:
                    if i == 0:
                        L[i][j] = L[i][j-1]
                    if j == 0:
                        L[i][j] = L[i-1][j]
                    else:
                        L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[len(L)-1][len(L[0])-1]

        # if they are the same then must be in lcs
        # if not, both does not belong | a belong to lcs or b belong to lcs



# s = Solution()
# text1 = "abcde"
# text2 = "ace"
# print(s.longestCommonSubsequence(text1, text2))

# text1 = "abc"
# text2 = "def"
# print(s.longestCommonSubsequence(text1, text2))


# text1 = "oxcpqrsvwf" #qr
# text2 = "shmtulqrypy" #qr
# print(s.longestCommonSubsequence(text1, text2)) #2

