#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (44.36%)
# Likes:    1347
# Dislikes: 52
# Total Accepted:    198.3K
# Total Submissions: 447K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#

# @lc code=start
class Solution:
    # def partition(self, s: str) -> List[List[str]]:
    def partition(self, s):
        n = len(s)
        res = []

        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(temp, start):
            # print('temp=', temp, "start=", start)
            if start == n:
                res.append(temp.copy())
            else:
                for i in range(start, n):
                    if isPalindrome(s, start, i):
                        temp.append(s[start: i + 1])
                        backtrack(temp, i + 1)
                        temp.pop()
                    
        backtrack([], 0)
        # print('res=', res)
        return res
# @lc code=end
