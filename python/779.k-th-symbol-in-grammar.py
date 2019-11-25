#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#
# https://leetcode.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (37.67%)
# Total Accepted:    18.1K
# Total Submissions: 48K
# Testcase Example:  '1\n1'
#
# On the first row, we write a 0. Now in every subsequent row, we look at the
# previous row and replace each occurrence of 0 with 01, and each occurrence of
# 1 with 10.
# 
# Given row N and index K, return the K-th indexed symbol in row N. (The values
# of K are 1-indexed.) (1 indexed).
# 
# 
# Examples:
# Input: N = 1, K = 1
# Output: 0
# 
# Input: N = 2, K = 1
# Output: 0
# 
# Input: N = 2, K = 2
# Output: 1
# 
# Input: N = 4, K = 5
# Output: 1
# 
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001
# 
# 
# Note:
# 
# 
# N will be an integer in the range [1, 30].
# K will be an integer in the range [1, 2^(N-1)].
# 
# 
#
class Solution:
    def kthGrammar2(self, N: int, K: int) -> int:
        
        def recur(N):
            if N == 1:
                return [0]
            else:
                prev = recur(N-1)
                return prev + [1-x for x in prev]


        return recur(N)[K-1]

    def kthGrammar(self, N: int, K: int) -> int:


        def recur(N, K):
            if N == 1:
                return 0

            
            half_length = 2 ** (N-2)
            if K > half_length:
                return 1 - recur(N-1, K - half_length)
            else:
                return recur(N-1, K)

        return recur(N, K)

# s = Solution()
# N = 4
# K = 5
# print(s.kthGrammar(N, K) == 1)


# N = 2
# K = 2
# print(s.kthGrammar(N, K) == 1)


# N = 2
# K = 1
# print(s.kthGrammar(N, K) == 0)


# N = 1
# K = 1
# print(s.kthGrammar(N, K) == 0)


# N = 30
# K = 434991989
# print(s.kthGrammar(N, K))




