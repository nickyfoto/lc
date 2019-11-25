#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (71.56%)
# Total Accepted:    21.8K
# Total Submissions: 30.4K
# Testcase Example:  '7'
#
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
# 
# Return a list of all possible full binary trees with N nodes.  Each element
# of the answer is the root node of one possible tree.
# 
# Each node of each tree in the answer must have node.val = 0.
# 
# You may return the final list of trees in any order.
# 
# 
# 
# Example 1:
# 
# 
# Input: 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 20
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def allPossibleFBT(self, N: int) -> List[TreeNode]:
    def allPossibleFBT(self, N):
        
        if N == 1:
            return [TreeNode(0)]

        if N % 2 == 0:
            return []

        res = []

        def makeTrees(l, r):
            res = []
            lefts, rights = self.allPossibleFBT(l), self.allPossibleFBT(r)
            # print(lefts, rights)
            for i in lefts:
                for j in rights:
                    node = TreeNode(0)
                    node.left = i
                    node.right = j
                    # print('node=', node)
                    res.append(node)
            return res        
        
        N -= 1
        for i in range(1, N,2):
            # print('i=', i)
            l, r = tuple((i, N-i))
            # print('l, r = ', l, r)
            nodes = makeTrees(l, r)
            # print('nodes=', nodes)
            res.extend(nodes)

        return res


# from tn import TreeNode
# s = Solution()
# results = s.allPossibleFBT(1)
# results = s.allPossibleFBT(3)
# results = s.allPossibleFBT(5)
# results = s.allPossibleFBT(7)
# print('results=', results)
# for i in results:
#     print(i)

# print(s.allPossibleFBT(2))
# print(s.allPossibleFBT(3))
# print(s.allPossibleFBT(5))
# print(s.allPossibleFBT(7))
