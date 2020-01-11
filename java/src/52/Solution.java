/*
 * @lc app=leetcode id=52 lang=java
 *
 * [52] N-Queens II
 *
 * https://leetcode.com/problems/n-queens-ii/description/
 *
 * algorithms
 * Hard (55.03%)
 * Likes:    376
 * Dislikes: 132
 * Total Accepted:    117.1K
 * Total Submissions: 212.8K
 * Testcase Example:  '4'
 *
 * The n-queens puzzle is the problem of placing n queens on an n×n chessboard
 * such that no two queens attack each other.
 * 
 * 
 * 
 * Given an integer n, return the number of distinct solutions to the n-queens
 * puzzle.
 * 
 * Example:
 * 
 * 
 * Input: 4
 * Output: 2
 * Explanation: There are two distinct solutions to the 4-queens puzzle as
 * shown below.
 * [
 * [".Q..",  // Solution 1
 * "...Q",
 * "Q...",
 * "..Q."],
 * 
 * ["..Q.",  // Solution 2
 * "Q...",
 * "...Q",
 * ".Q.."]
 * ]
 * 
 * 
 */

// @lc code=start
class Solution {
    int res = 0;

    private void backtrack(int n, boolean[] v, boolean[] l, boolean[] r, int row) {
        if (row == n) {
            res += 1;
        }
        for (int col = 0; col < n; col++) {
            if (v[col] || l[row - col + n] || r[row+col]) {
                continue;
            }
            v[col] = true;
            l[row - col + n] = true;
            r[row + col] = true;
            backtrack(n, v, l, r, row + 1);
            v[col] = false;
            l[row - col + n] = false;
            r[row + col] = false;
        }
    }
    
    public int totalNQueens(int n) {
        
        boolean[] v = new boolean[n];
        boolean[] l = new boolean[2 * n];
        boolean[] r = new boolean[2 * n];
        backtrack(n, v, l, r, 0);
        return res;
    }

    public static void main(String args[]) {
        Solution s = new Solution();
        int n = 4;
        System.out.println(s.totalNQueens(n));
    }
}
// @lc code=end
