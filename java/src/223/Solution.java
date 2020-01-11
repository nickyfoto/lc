/*
 * @lc app=leetcode id=223 lang=java
 *
 * [223] Rectangle Area
 *
 * https://leetcode.com/problems/rectangle-area/description/
 *
 * algorithms
 * Medium (36.87%)
 * Likes:    318
 * Dislikes: 602
 * Total Accepted:    97.6K
 * Total Submissions: 264.6K
 * Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
 *
 * Find the total area covered by two rectilinear rectangles in a 2D plane.
 * 
 * Each rectangle is defined by its bottom left corner and top right corner as
 * shown in the figure.
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
 * Output: 45
 * 
 * Note:
 * 
 * Assume that the total area is never beyond the maximum possible value of
 * int.
 * 
 */

// @lc code=start
class Solution {


    private boolean overlap(int A, int B, int C, int D, int E, int F, int G, int H) {
        if (A >= G || E >= C) return false;
        if (B >= H || F >= D) return false;
        return true;
    }

    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int a1 = (C - A) * (D - B);
        int a2 = (G - E) * (H - F);
        // System.out.println(a1);
        // System.out.println(a2);

        int llx = Math.max(A, E);
        int lly = Math.max(B, F);
        int urx = Math.min(C, G);
        int ury = Math.min(D, H);
        if (overlap(A, B, C, D, E, F, G, H)) {
            int c = (urx - llx) * (ury - lly);
            return a1 + a2 - c;
        }
        return a1 + a2;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int res = s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2);
        System.out.println(res);
        res = s.computeArea(-2, -2, 2, 2, -3, -3, 3, -1);
        System.out.println(res);
        res = s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4);
        System.out.println(res);
    }
}
// @lc code=end
