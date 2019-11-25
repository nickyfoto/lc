#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (29.62%)
# Total Accepted:    221.2K
# Total Submissions: 740.9K
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which will return whether
# version is bad. Implement a function to find the first bad version. You
# should minimize the number of calls to the API.
# 
# Example:
# 
# 
# Given n = 5, and version = 4 is the first bad version.
# 
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# 
# Then 4 is the first bad version. 
# 
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version >= 2:
        return True
    return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        def bs(low, high):
            firstFalse = low + (high-low) // 2
            if isBadVersion(firstFalse) and isBadVersion(firstFalse-1):
                # guess to big
                return bs(low, firstFalse)
            elif not isBadVersion(firstFalse) and not isBadVersion(firstFalse-1):
                # guess to small
                # print(isBadVersion(firstFalse), isBadVersion(firstFalse-1))
                if high - firstFalse == 1:
                    return bs(firstFalse, high+1)
                else:
                    return bs(firstFalse, high)
            else:
                return firstFalse
        return bs(0, n)




s = Solution()
# print(s.firstBadVersion(5))
print(s.firstBadVersion(2))














        
