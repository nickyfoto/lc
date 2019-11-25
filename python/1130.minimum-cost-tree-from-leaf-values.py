#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/
#
# algorithms
# Medium (58.60%)
# Total Accepted:    4.8K
# Total Submissions: 8.2K
# Testcase Example:  '[6,2,4]'
#
# Given an array arr of positive integers, consider all binary trees such
# that:
# 
# 
# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order
# traversal of the tree.  (Recall that a node is a leaf if and only if it has 0
# children.)
# The value of each non-leaf node is equal to the product of the largest leaf
# value in its left and right subtree respectively.
# 
# 
# Among all possible binary trees considered, return the smallest possible sum
# of the values of each non-leaf node.  It is guaranteed this sum fits into a
# 32-bit integer.
# 
# 
# Example 1:
# 
# 
# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the
# second has non-leaf node sum 32.
# 
# ⁠   24            24
# ⁠  /  \          /  \
# ⁠ 12   4        6    8
# ⁠/  \               / \
# 6    2             2   4
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is
# less than 2^31).
# 
#
class Solution:
    # def mctFromLeafValues(self, arr: List[int]) -> int:
    def mctFromLeafValues(self, arr):
        n = len(arr)
        # mini = float('inf')
        l = []
        
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def recur(arr):
            n = len(arr)
            if n == 1:
                return 0
            if n == 2:
                return arr[0] * arr[1]
            else:
                l = []
                for i in range(1, n):
                    res = max(arr[:i]) * max(arr[i:]) + recur(arr[:i]) + recur(arr[i:])
                    l.append(res)
                    # print('here', i, arr[:i], arr[i:], l)
                return min(l)
        # print()
        return recur(tuple(arr))
        


# s = Solution()
# arr = [6,2,4]
# arr = [6,2,4,1]
# arr = [1,2,4,6]
# arr = [7,12,8,10]
# print(s.mctFromLeafValues(arr))


# arr = [10,14,7,10,6,14,4,14,4,4,4,15,7,4,9]
# print(s.mctFromLeafValues(arr))












        
