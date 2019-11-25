#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (42.88%)
# Total Accepted:    576.9K
# Total Submissions: 1.3M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        l = []
        while x > 0:
            d, r = divmod(x, 10)
            # print(d, r)
            l.append(r)
            x = d
        
        # print(l)
        for i in range(len(l)):
            # print(i, l[i], l[-i], l)
            if i < len(l) // 2 and l[i] != l[-(i+1)]:
                return False
        return True

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(123))

        
