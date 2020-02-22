#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string/description/
#
# algorithms
# Hard (32.81%)
# Likes:    394
# Dislikes: 620
# Total Accepted:    101.9K
# Total Submissions: 310.4K
# Testcase Example:  '"great"\n"rgeat"'
#
# Given a string s1, we may represent it as a binary tree by partitioning it to
# two non-empty substrings recursively.
# 
# Below is one possible representation of s1 = "great":
# 
# 
# ⁠   great
# ⁠  /    \
# ⁠ gr    eat
# ⁠/ \    /  \
# g   r  e   at
# ⁠          / \
# ⁠         a   t
# 
# 
# To scramble the string, we may choose any non-leaf node and swap its two
# children.
# 
# For example, if we choose the node "gr" and swap its two children, it
# produces a scrambled string "rgeat".
# 
# 
# ⁠   rgeat
# ⁠  /    \
# ⁠ rg    eat
# ⁠/ \    /  \
# r   g  e   at
# ⁠          / \
# ⁠         a   t
# 
# 
# We say that "rgeat" is a scrambled string of "great".
# 
# Similarly, if we continue to swap the children of nodes "eat" and "at", it
# produces a scrambled string "rgtae".
# 
# 
# ⁠   rgtae
# ⁠  /    \
# ⁠ rg    tae
# ⁠/ \    /  \
# r   g  ta  e
# ⁠      / \
# ⁠     t   a
# 
# 
# We say that "rgtae" is a scrambled string of "great".
# 
# Given two strings s1 and s2 of the same length, determine if s2 is a
# scrambled string of s1.
# 
# Example 1:
# 
# 
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
# 
#

# @lc code=start
class Solution:
    # def isScramble(self, s1: str, s2: str) -> bool:
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        count = [0] * 26
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]):
                if self.isScramble(s1[i:], s2[i:]):
                    return True
            if self.isScramble(s1[:i], s2[-i:]):
                if self.isScramble(s1[i:], s2[:-i]):
                    return True
        return False
# @lc code=end
