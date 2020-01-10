/*
 * @lc app=leetcode id=869 lang=java
 *
 * [869] Reordered Power of 2
 *
 * https://leetcode.com/problems/reordered-power-of-2/description/
 *
 * algorithms
 * Medium (51.75%)
 * Likes:    162
 * Dislikes: 76
 * Total Accepted:    11.9K
 * Total Submissions: 22.9K
 * Testcase Example:  '1'
 *
 * Starting with a positive integer N, we reorder the digits in any order
 * (including the original order) such that the leading digit is not zero.
 * 
 * Return true if and only if we can do this in a way such that the resulting
 * number is a power of 2.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: 1
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: 10
 * Output: false
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: 16
 * Output: true
 * 
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: 24
 * Output: false
 * 
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: 46
 * Output: true
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= N <= 10^9
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
import java.util.HashMap;

class Solution {


    private HashMap<Character, Integer> toHashMap(String s) {
        char[] chars = s.toCharArray();
        HashMap<Character, Integer> nc = new HashMap<Character, Integer>();

        for (Character a : chars) {
            if (nc.containsKey(a)) {
                int oldValue = nc.get(a);
                nc.put(a, oldValue + 1);
            } else {
                nc.put(a, 1);
            }
        }
        return nc;
    }

    public boolean reorderedPowerOf2(int N) {
        String sn = Integer.toString(N);

        int l = sn.length();

        HashMap<Character, Integer> nc = toHashMap(sn);



        int i = 0;
        String p2 = Integer.toString( (int) Math.pow((float) 2, (float) i));
        while (p2.length() <= l) {
//            System.out.println(nc.equals(toHashMap(p2)));
//            System.out.println(toHashMap(p2));
            if (p2.length() == l && toHashMap(p2).equals( nc )) return true;
            i += 1;
            p2 = Integer.toString( (int) Math.pow((float) 2, (float) i));
        }
        return false;

    }

    public static void main(String args[]) {
        Solution s = new Solution();
        System.out.println(s.reorderedPowerOf2(1));
    }
}
// @lc code=end
