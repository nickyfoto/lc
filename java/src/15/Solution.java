

/*
 * @lc app=leetcode id=15 lang=java
 *
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (25.58%)
 * Likes:    5399
 * Dislikes: 658
 * Total Accepted:    756.2K
 * Total Submissions: 3M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the
 * sum of zero.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate triplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 0, 1, 2, -1, -4],
 * 
 * A solution set is:
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 */

// @lc code=start
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        for (int i = 0; i < nums.length - 2; i++) {
            if (i == 0 || i > 0 && nums[i-1] != nums[i]) {
                int left = i + 1;
                int right = n - 1;
                int sm = 0 - nums[i];
                while (left < right) {
                    if (nums[left] + nums[right] == sm) {
                        res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) left += 1;
                        while (left < right && nums[right - 1] == nums[right]) right -= 1;
                        left += 1;
                        right -= 1;
                    } else if (nums[left] + nums[right] < sm) left += 1;
                    else right -= 1;
                }
            }
        }
        return res;
    }
}
// @lc code=end
