#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (49.01%)
# Total Accepted:    119K
# Total Submissions: 242.7K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
# 
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# 
# 
# Input: [3,4,5,1,3,null,1]
# 
#     3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def rob(self, root: TreeNode) -> int:
    def rob2(self, root) -> int:
        if not root:
            return 0
        q = [[root]]
        # level = 0
        record = []
        while q:
            nodes = q.pop(0)
            record.append(sum(n.val for n in nodes))
            new_nodes = []
            for n in nodes:
                if n.left:
                    new_nodes.append(n.left)
                if n.right:
                    new_nodes.append(n.right)
            if new_nodes:
                q.append(new_nodes)
        print(record)
        

        L = record.copy()
        for i in range(len(L)):
            if i - 1 > 0:
                # print(i, L[:i-1])
                L[i] += max(L[:i-1])
        # print(L)
        return max(L)


    def rob(self, root) -> int:
        if not root:
            return 0
        def isLeaf(node):
            return not node.left and not node.right

        self.mx = root.val

        def dfs(node):
            if node:

                ind_l, d_l = dfs(node.left)
                ind_r, d_r = dfs(node.right)
                

                if isLeaf(node):
                    node.d = node.val
                    node.ind = 0

                elif node.left and node.right:
                    node.ind = max(node.left.d, node.left.ind) + max(node.right.d, node.right.ind)

                                    
                    node.d = node.val + node.left.ind + node.right.ind
                elif node.left and not node.right:
                    node.ind = max(node.left.d, node.left.ind)
                    node.d = node.val + node.left.ind
                elif node.right and not node.left:
                    node.ind = max(node.right.d, node.right.ind)
                    node.d = node.val + node.right.ind
                # print(node.val)
                # print(node.val, 'd=', node.d, 'ind=', node.ind)
                self.mx = max(self.mx, max(node.d, node.ind))
                return ind_l + ind_r, d_l + d_r
            else:
                return 0, 0

        dfs(root)

        
        # def find_mx(node):
        #     if node:
        #         self.mx = max(max(node.d, node.ind), self.mx)
        #         find_mx(node.left)
        #         find_mx(node.right)
        # find_mx(root)
        # print(self.mx)
        return self.mx


s = Solution()
from tn import buildRoot, null
l = [3,2,3,null,3,null,1]
root = buildRoot(l)
print(s.rob(root) == 7)


l = [3,4,5,1,3,null,1]

root = buildRoot(l)
print(s.rob(root) == 9)



l = [4,1,null,2,null,3]
root = buildRoot(l)
print(s.rob(root) == 7)




l = [2,1,3,null,4]
root = buildRoot(l)
print(s.rob(root) == 7)



l = [41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]
root = buildRoot(l)
print(s.rob(root) == 690) #690



        
