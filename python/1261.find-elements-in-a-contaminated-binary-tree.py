#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
#
# algorithms
# Medium (72.59%)
# Likes:    57
# Dislikes: 13
# Total Accepted:    5.9K
# Total Submissions: 8.2K
# Testcase Example:  '["FindElements","find","find"]\r\n[[[-1,null,-1]],[1],[2]]\r'
#
# Given a binary tree with the following rules:
# 
# 
# root.val == 0
# If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 *
# x + 1
# If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2
# * x + 2
# 
# 
# Now the binary tree is contaminated, which means all treeNode.val have been
# changed to -1.
# 
# You need to first recover the binary tree and then implement the FindElements
# class:
# 
# 
# FindElements(TreeNode* root) Initializes the object with a contamined binary
# tree, you need to recover it first.
# bool find(int target) Return if the target value exists in the recovered
# binary tree.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# Output
# [null,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1]); 
# findElements.find(1); // return False 
# findElements.find(2); // return True 
# 
# Example 2:
# 
# 
# 
# 
# Input
# ["FindElements","find","find","find"]
# [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
# Output
# [null,true,true,false]
# Explanation
# FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
# findElements.find(1); // return True
# findElements.find(3); // return True
# findElements.find(5); // return False
# 
# Example 3:
# 
# 
# 
# 
# Input
# ["FindElements","find","find","find","find"]
# [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
# Output
# [null,true,false,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
# findElements.find(2); // return True
# findElements.find(3); // return False
# findElements.find(4); // return False
# findElements.find(5); // return True
# 
# 
# 
# Constraints:
# 
# 
# TreeNode.val == -1
# The height of the binary tree is less than or equal to 20
# The total number of nodes is between [1, 10^4]
# Total calls of find() is between [1, 10^4]
# 0 <= target <= 10^6
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
# from lcpy import TreeNode, null, buildRoot

class FindElements:

    def is_leaf(self, node):
        return not node.left and not node.right

    def recover(self, root):
        if not root:
            return
        x = root.val
        if root.left:
            root.left.val = 2 * x + 1
        if root.right:
            root.right.val = 2 * x + 2
        self.recover(root.right)
        self.recover(root.left)

    def __init__(self, root: TreeNode):
        # print(root)
        # print(root.bfs_null())
        self.root = root
        self.root.val = 0
        self.recover(self.root)
        # print(root.bfs_null())

    def get_path(self, target):
        path = []
        def recur(n):
            q, r = divmod(n, 2)
            if r == 1:
                path.append('l')
                if q == 0:
                    return
                recur(q)
            else:
                path.append('r')
                if q == 1:
                    return
                recur(q - 1)
        recur(target)
        return path
    def find(self, target: int) -> bool:
        
        path = self.get_path(target) 
        # print(path)

        def search(node, path):
            if node is None:
                return False
            if node.val == target:
                return True
            else:
                if path:
                    branch = path.pop()
                    if branch == 'l':
                        return search(node.left, path)
                    else:
                        return search(node.right, path)
                else:
                    return False
        return search(self.root, path)




# Your FindElements object will be instantiated and called as such:
# root = buildRoot([-1,null,-1])
# obj = FindElements(root)
# print(obj.find(1))
# print(obj.find(2))

# print("="*80)
# root = buildRoot([-1,-1,-1,-1,-1])
# obj = FindElements(root)
# print(obj.find(1))
# print(obj.find(3))
# print(obj.find(5))

# print("="*80)
# root = buildRoot([-1,null,-1,-1,null,-1])
# obj = FindElements(root)
# print(obj.find(2))
# print(obj.find(3))
# print(obj.find(4))
# print(obj.find(5))


# param_1 = obj.find(target)
# @lc code=end
