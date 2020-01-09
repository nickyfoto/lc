/*
 * @lc app=leetcode id=1302 lang=java
 *
 * [1302] Deepest Leaves Sum
 *
 * https://leetcode.com/problems/deepest-leaves-sum/description/
 *
 * algorithms
 * Medium (85.27%)
 * Likes:    94
 * Dislikes: 11
 * Total Accepted:    8.1K
 * Total Submissions: 9.5K
 * Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
 *
 * Given a binary tree, return the sum of values of its deepest leaves.
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
 * Output: 15
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is between 1 and 10^4.
 * The value of nodes is between 1 and 100.
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


import java.util.LinkedList;
import java.util.Queue;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int deepestLeavesSum(TreeNode root) {
        int res = 0;
        boolean dl;
        List<TreeNode> nodes = new ArrayList<TreeNode>();
        nodes.add(root);
        Queue<List<TreeNode>> q = new LinkedList<List<TreeNode>>();
        q.add(nodes);

        while (q.peek() != null) {
            nodes = q.remove();
            List<TreeNode> l = new ArrayList<TreeNode>();
            dl = true;
            for (TreeNode node : nodes) {
                if (node.left != null || node.right != null) {
                    dl = false;
                    res = 0;
                    if (node.left != null) l.add(node.left);
                    if (node.right != null) l.add(node.right);
                } else {
                    if (dl == true) res += node.val;
                    else res = 0;
                }
            }

            if (l.isEmpty() == false) q.add(l);
        }
        return res;
    }

    public static void main(String args[]) {
        System.out.println("ok");
    }
}
// @lc code=end
