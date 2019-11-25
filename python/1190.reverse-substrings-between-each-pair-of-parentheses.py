#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
#
# algorithms
# Medium (56.09%)
# Total Accepted:    4.9K
# Total Submissions: 8.5K
# Testcase Example:  '"(abcd)"'
#
# Given a string s that consists of lower case English letters and brackets. 
# 
# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.
# 
# Your result should not contain any bracket.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "(abcd)"
# Output: "dcba"
# 
# 
# Example 2:
# 
# 
# Input: s = "(u(love)i)"
# Output: "iloveu"
# 
# 
# Example 3:
# 
# 
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# 
# 
# Example 4:
# 
# 
# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It's guaranteed that all parentheses are balanced.
# 
# 
#
class Solution:
    def reverseParentheses(self, s: str) -> str:
        


        parentheses_stack = []
        word_stack = []
        res = []
        s = list(s)
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                parentheses_stack.append(i)
            if s[i] == ')':
                left = parentheses_stack.pop()
                right = i
                # print(left, right)
                # print(s[left:right+1])
                s[left:right+1] = s[left:right+1][::-1]
        s = [x for x in s if x != '(' and x != ')']
        # print("".join(s))


        return "".join(s)







# S = Solution()
# s = "a(bcdefghijkl(mno)p)q"
# print(S.reverseParentheses(s) == "apmnolkjihgfedcbq")


# s = "(ed(et(oc))el)"
# print(S.reverseParentheses(s) == "leetcode")

# s = "(u(love)i)"
# print(S.reverseParentheses(s) == "iloveu")


# s = "(abcd)"
# print(S.reverseParentheses(s) == "dcba")






