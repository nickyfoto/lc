#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (58.39%)
# Total Accepted:    70.1K
# Total Submissions: 120.1K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# Output: [1, 3, 9]
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
    # def largestValues(self, root: TreeNode) -> List[int]:
    def largestValues(self, root):
        if not root:
            return []
        # print(root)
        res = []
        q = [[root]]
        while q:
            l = q.pop(0)
            res.append(max([n.val for n in l]))
            children = []
            for node in l:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            if children:
                q.append(children)
        # print(res)
        return res



# from tn import buildRoot, null

# s = Solution()
# l = [1,3,2,5,3,null,9]
# root = buildRoot(l)
# print(s.largestValues(root))
