/*
 * @lc app=leetcode id=387 lang=java
 *
 * [387] First Unique Character in a String
 *
 * https://leetcode.com/problems/first-unique-character-in-a-string/description/
 *
 * algorithms
 * Easy (51.39%)
 * Likes:    1451
 * Dislikes: 99
 * Total Accepted:    383.4K
 * Total Submissions: 746K
 * Testcase Example:  '"leetcode"'
 *
 * 
 * Given a string, find the first non-repeating character in it and return it's
 * index. If it doesn't exist, return -1.
 * 
 * Examples:
 * 
 * s = "leetcode"
 * return 0.
 * 
 * s = "loveleetcode",
 * return 2.
 * 
 * 
 * 
 * 
 * Note: You may assume the string contain only lowercase letters.
 * 
 */

// @lc code=start
import java.util.HashMap;

class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> c = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            c.put(s.charAt(i), c.getOrDefault(s.charAt(i), 0) + 1);
        }
        for (int i = 0; i < s.length(); i++) {
            if (c.get(s.charAt(i)) == 1) return i;
        }
        return -1;
    }
    
}
// import java.util.TreeMap;
// class Solution {
//     public int firstUniqChar(String s) {
//         TreeMap<Character, Integer> counter = new TreeMap<>();
//         for (int i = 0; i < s.length(); i++) {
//             if (counter.containsKey(s.charAt(i))) counter.put(s.charAt(i), counter.get(s.charAt(i)) + 1);
//             else counter.put(s.charAt(i), 1);
//         }
//         for (int i = 0; i < s.length(); i++) {
//             if (counter.get(s.charAt(i)) == 1) return i;
//         }
//         return -1;
//     }
// }
// @lc code=end
