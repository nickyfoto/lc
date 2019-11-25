#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.33%)
# Total Accepted:    412K
# Total Submissions: 994.6K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#
class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        self.l = digits
        def recur(idx, num):
            # print(self.l, idx, num)
            if idx == -1:
                return
            res = self.l[idx] + num
            if res < 10:
                self.l[idx] = res
                recur(idx - 1, 0)
            else:
                if idx == 0:
                    self.l[idx] = res - 10
                    self.l.insert(0, 1)
                else:
                    self.l[idx] = res - 10
                    recur(idx - 1, 1)
        n = len(digits)
        recur(n-1, 1)
        return self.l
# s = Solution()
# digits = [1,2,3]
# print(s.plusOne(digits))

# digits = [4,3,2,1]
# print(s.plusOne(digits))
# digits = [9,9,9]
# print(s.plusOne(digits))