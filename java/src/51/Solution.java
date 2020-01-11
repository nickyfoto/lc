/*
 * @lc app=leetcode id=51 lang=java
 *
 * [51] N-Queens
 *
 * https://leetcode.com/problems/n-queens/description/
 *
 * algorithms
 * Hard (43.08%)
 * Likes:    1358
 * Dislikes: 61
 * Total Accepted:    173.3K
 * Total Submissions: 402.3K
 * Testcase Example:  '4'
 *
 * The n-queens puzzle is the problem of placing n queens on an n×n chessboard
 * such that no two queens attack each other.
 * 
 * 
 * 
 * Given an integer n, return all distinct solutions to the n-queens puzzle.
 * 
 * Each solution contains a distinct board configuration of the n-queens'
 * placement, where 'Q' and '.' both indicate a queen and an empty space
 * respectively.
 * 
 * Example:
 * 
 * 
 * Input: 4
 * Output: [
 * ⁠[".Q..",  // Solution 1
 * ⁠ "...Q",
 * ⁠ "Q...",
 * ⁠ "..Q."],
 * 
 * ⁠["..Q.",  // Solution 2
 * ⁠ "Q...",
 * ⁠ "...Q",
 * ⁠ ".Q.."]
 * ]
 * Explanation: There exist two distinct solutions to the 4-queens puzzle as
 * shown above.
 * 
 * 
 */

// @lc code=start
import java.util.List;
import java.util.ArrayList;

class Solution {
    List<List<String>> ret = new ArrayList<>();
    private void backtrack(int n, boolean[] v, boolean[] l, boolean[] r,
                             int row, char[][] s) {
        if (row == n) {
            List<String> toAdd = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                toAdd.add(String.valueOf(s[i]));
            }
            ret.add(toAdd);
            return;
        }

        for (Integer col = 0; col < n; col++) {
            if (v[col] || l[row - col + n] || r[row+col]) {
                continue;
            }
            v[col] = true;
            l[row - col + n] = true;
            r[row + col] = true;
            s[row][col] = 'Q';
            backtrack(n, v, l, r, row + 1, s);
            v[col] = false;
            l[row - col + n] = false;
            r[row + col] = false;
            s[row][col] = '.';
        }
    }

    public List<List<String>> solveNQueens(int n) {
        boolean[] v = new boolean[n];
        boolean[] l = new boolean[2 * n];
        boolean[] r = new boolean[2 * n];
        
        char[][] curr = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                curr[i][j] = '.';
            }
        }
        backtrack(n, v, l, r, 0, curr);
        return ret;
    }


    public static void main(String args[]) {
        Solution s = new Solution();
        int n = 4;
        System.out.println(s.solveNQueens(n));
    }
}
// @lc code=end
