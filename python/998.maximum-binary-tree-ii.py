#
# @lc app=leetcode id=998 lang=python3


class Solution:
    # def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
    def insertIntoMaxTree(self, root, val):



        def add_val_to_root(root, val):
            if val > root.val:
                node = TreeNode(val)
                node.left = root
                return node
            else:
                if root.left:
                    root.left = add_val_to_root(root.left, val)
                    return root
                elif root.right:
                    root.right = add_val_to_root(root.left, val)
                    return root
                else:
                    node = TreeNode(val)
                    root.left = node
                    return root


        return add_val_to_root(root, val)



s = Solution()
from tn import buildRoot, null, TreeNode
root = [5,2,4,null,1]
val = 3
root = buildRoot(root)

print(s.insertIntoMaxTree(root, val))








        
