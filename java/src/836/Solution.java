/*
 * @lc app=leetcode id=836 lang=java
 *
 * [836] Rectangle Overlap
 *
 * https://leetcode.com/problems/rectangle-overlap/description/
 *
 * algorithms
 * Easy (48.15%)
 * Likes:    485
 * Dislikes: 93
 * Total Accepted:    37.7K
 * Total Submissions: 78.3K
 * Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
 *
 * A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are
 * the coordinates of its bottom-left corner, and (x2, y2) are the coordinates
 * of its top-right corner.
 * 
 * Two rectangles overlap if the area of their intersection is positive.  To be
 * clear, two rectangles that only touch at the corner or edges do not
 * overlap.
 * 
 * Given two (axis-aligned) rectangles, return whether they overlap.
 * 
 * Example 1:
 * 
 * 
 * Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
 * Output: false
 * 
 * 
 * Notes:
 * 
 * 
 * Both rectangles rec1 and rec2 are lists of 4 integers.
 * All coordinates in rectangles will be between -10^9 and 10^9.
 * 
 * if one rec1 is on the left of the other or one is above of the other return false
 */

// @lc code=start
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {

        if (rec1[0]>=rec2[2] || rec2[0]>=rec1[2]) return false;
        if (rec1[1]>=rec2[3] || rec2[1]>=rec1[3]) return false;
        return true;
    }
}
// @lc code=end