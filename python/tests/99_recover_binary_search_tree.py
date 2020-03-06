#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (37.45%)
# Likes:    1211
# Dislikes: 66
# Total Accepted:    146.2K
# Total Submissions: 389.4K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# Example 1:
# 
# 
# Input: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# Output: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# Output: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 
# Follow up:
# 
# 
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def recoverTree(self, root: TreeNode) -> None:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        def find_two_swapped(nums):
            x = y = -1
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y
        def recover(node, count):
            if node:
                if node.val == x or node.val == y:
                    node.val = y if node.val == x else x
                    count -= 1
                    if count == 0:
                        return 
                recover(node.left, count)
                recover(node.right, count)
        nums = inorder(root)
        x, y = find_two_swapped(nums)
        recover(root, 2)
        
# @lc code=end
