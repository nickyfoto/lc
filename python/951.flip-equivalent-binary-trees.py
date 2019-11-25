#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (64.87%)
# Total Accepted:    21.9K
# Total Submissions: 33.8K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
# 
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
# 
# Write a function that determines whether two binary trees are flip
# equivalent.  The trees are given by root nodes root1 and root2.
# 
# 
# 
# Example 1:
# 
# 
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
# 
# 
# 
# 
# 
# Note:
# 
# 
# Each tree will have at most 100 nodes.
# Each value in each tree will be a unique integer in the range [0, 99].
# 
# 
# 
# 
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
    # def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
    def flipEquiv(self, root1, root2):

        # print(root1, root2)

        def equal_in_val(n1, n2):
            #only compare two node, not their children
            # if not n1 and not n2:
                # return True
            # if n1 and n2:
                # print(n1.val, n2.val)
            if n1 and not n2:
                return False
            if n2 and not n1:
                return False
            # print(n1.val, n2.val)
            return n1.val == n2.val
                



        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if equal_in_val(node1, node2):
                return (dfs(node1.left, node2.left) and dfs(node1.right, node2.right)) or (dfs(node1.left, node2.right) and dfs(node1.right, node2.left))
            return False    
            



        return dfs(root1, root2)




# from tn import null, buildRoot
# s = Solution()

# root1 = [1,2,3,4,5,6,null,null,null,7,8]
# root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# root1 = buildRoot(root1)
# root2 = buildRoot(root2)

# print(s.flipEquiv(root1, root2))





# root1 = [1,2,3,4,5,6,null,null,null,7,8]
# root2 = [1,3,2,null,6,4,5,null,null,null,null,8]
# root1 = buildRoot(root1)
# root2 = buildRoot(root2)

# print(s.flipEquiv(root1, root2))







        
