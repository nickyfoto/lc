#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (76.26%)
# Total Accepted:    90K
# Total Submissions: 117.4K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
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
    # def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    def constructMaximumBinaryTree(self, nums):
        def build(nums):
            m_idx = [idx for idx, v in enumerate(nums) if v == max(nums)][0]
            # print(m_idx)
            node = TreeNode(nums[m_idx])
            if nums[:m_idx]:
                node.left = build(nums[:m_idx])
            if nums[m_idx+1:]:
                node.right = build(nums[m_idx+1:])
            return node
        # m_idx = 
        return build(nums)

# s = Solution()
# nums = [3,2,1,6,0,5]
# print(s.constructMaximumBinaryTree(nums))
