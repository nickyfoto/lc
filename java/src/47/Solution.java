/*
 * @lc app=leetcode id=47 lang=java
 *
 * [47] Permutations II
 *
 * https://leetcode.com/problems/permutations-ii/description/
 *
 * algorithms
 * Medium (43.81%)
 * Likes:    1507
 * Dislikes: 52
 * Total Accepted:    303.7K
 * Total Submissions: 693.2K
 * Testcase Example:  '[1,1,2]'
 *
 * Given a collection of numbers that might contain duplicates, return all
 * possible unique permutations.
 * 
 * Example:
 * 
 * 
 * Input: [1,1,2]
 * Output:
 * [
 * ⁠ [1,1,2],
 * ⁠ [1,2,1],
 * ⁠ [2,1,1]
 * ]
 * 
 * 
 */

// @lc code=start
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    private void backtrack(List<List<Integer>> lst, List<Integer> temp, int[] nums, boolean[] used) {
        if (temp.size() == nums.length) lst.add(new ArrayList<>(temp));
        else {
            for (int i = 0; i < nums.length; i++) {
                if (used[i] || i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
                used[i] = true;
                temp.add(nums[i]);
                backtrack(lst, temp, nums, used);
                used[i] = false;
                temp.remove(temp.size() - 1);

            }
        }
    }
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> lst = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(lst, new ArrayList<>(), nums, new boolean[nums.length]);
        return lst;
    }
}
// @lc code=end
