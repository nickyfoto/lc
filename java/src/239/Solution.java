/*
 * @lc app=leetcode id=239 lang=java
 *
 * [239] Sliding Window Maximum
 *
 * https://leetcode.com/problems/sliding-window-maximum/description/
 *
 * algorithms
 * Hard (40.62%)
 * Likes:    2520
 * Dislikes: 148
 * Total Accepted:    218.8K
 * Total Submissions: 538.7K
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * Given an array nums, there is a sliding window of size k which is moving
 * from the very left of the array to the very right. You can only see the k
 * numbers in the window. Each time the sliding window moves right by one
 * position. Return the max sliding window.
 * 
 * Example:
 * 
 * 
 * Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
 * Output: [3,3,5,5,6,7] 
 * Explanation: 
 * 
 * Window position                Max
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 * ⁠1 [3  -1  -3] 5  3  6  7       3
 * ⁠1  3 [-1  -3  5] 3  6  7       5
 * ⁠1  3  -1 [-3  5  3] 6  7       5
 * ⁠1  3  -1  -3 [5  3  6] 7       6
 * ⁠1  3  -1  -3  5 [3  6  7]      7
 * 
 * 
 * Note: 
 * You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
 * array.
 * 
 * Follow up:
 * Could you solve it in linear time?
 */

// @lc code=start
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Arrays;
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) return new int[0];
        
        Deque<Integer> d = new ArrayDeque<>();
        int n = nums.length;
        int[] res = new int[n - k + 1];
        
        for (int i = 0; i < nums.length; i++) {
            while (!d.isEmpty() && nums[d.peekLast()] < nums[i]) d.pollLast();
            d.addLast(i);
            if (d.peekFirst() == i - k) d.pollFirst();
            if (i >= k - 1) res[i - (k - 1)] = nums[d.peekFirst()];
        }
        return res;

    }

    // public static void main(String[] args) {
    //     int[] nums = {1,3,-1,-3,5,3,6,7};
    //     int k = 3;
    //     System.out.println(Arrays.toString(maxSlidingWindow(nums, k)));
    // }
}
// @lc code=end
