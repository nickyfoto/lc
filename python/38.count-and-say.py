#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (40.70%)
# Total Accepted:    294.3K
# Total Submissions: 718.2K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 6.     312211
# 7.     13112221
# 8.     1113213211
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution:
    # def countAndSay(self, n: int) -> str:
    def countAndSay(self, n: int) -> str:
        # if n == 1:
            # return "1"
        def count(s):
            n = len(s)
            i = 0
            start = s[0]
            count = 0
            res = ""
            while i < n:
                while i < n and s[i] == start:
                    count += 1
                    i += 1
                # print('start=', start)
                res += str(count) + str(start)
                count = 0
                if i < n:
                    start = s[i]
                    # print(count, start, 'i=', i, 's=', s, 'start=', start, self.res)
                # i += 1

                # count = 0
                # if i < n:
                    # start = s[i]
            return res
        self.res = ["1"]
        for i in range(1,n):
            self.res.append(count(self.res[i-1]))
        # print(self.res)

        return self.res[-1]

# s = Solution()
# print(s.countAndSay(4))
# print(s.countAndSay(5))
# print(s.countAndSay(6))
# print(s.countAndSay(7))
# print(s.countAndSay(8))