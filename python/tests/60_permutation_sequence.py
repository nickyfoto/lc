#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (35.01%)
# Likes:    1135
# Dislikes: 282
# Total Accepted:    161.7K
# Total Submissions: 461.7K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#

# @lc code=start
from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if k == 1:
            return "".join(map( str, range(1, n+1)))
        elif k == factorial(n):
            return self.getPermutation(n, 1)[::-1]
        
        k -= 1
        res = []
        numbers = list(range(1, n+1))
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            res.append(str(numbers[index]))
            numbers.remove(numbers[index])
        return "".join(res)

# @lc code=end
