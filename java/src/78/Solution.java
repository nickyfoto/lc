
/*
* @lc app=leetcode id=78 lang=java
*
* [78] Subsets
*
* https://leetcode.com/problems/subsets/description/
*
* algorithms
* Medium (57.36%)
* Likes:    2796
* Dislikes: 66
* Total Accepted:    471K
* Total Submissions: 821.1K
* Testcase Example:  '[1,2,3]'
*
* Given a set of distinct integers, nums, return all possible subsets (the
* power set).
* 
* Note: The solution set must not contain duplicate subsets.
* 
* Example:
* 
* 
* Input: nums = [1,2,3]
* Output:
* [
    * ⁠ [3],
    * [1],
    * [2],
    * [1,2,3],
    * [1,3],
    * [2,3],
    * [1,2],
    * []
    * ]
    * 
    */
    
    // @lc code=start
import java.util.ArrayList;
import java.util.Arrays;
class Solution {

    private void backtrack(List<List<Integer>> lst, List<Integer> temp, int[] nums, int start) {
        lst.add(new ArrayList<>(temp));
        for (int i = start; i < nums.length; i++) {
            temp.add(nums[i]);
            backtrack(lst, temp, nums, i + 1);
            temp.remove(temp.size() - 1);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> lst = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(lst, new ArrayList<>(), nums, 0);
        return lst;
    }
}
// @lc code=end
