#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (48.29%)
# Likes:    465
# Dislikes: 6
# Total Accepted:    31.6K
# Total Submissions: 65.4K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
# 
# 
# Example 1:
# 
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
# 
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
# 
#

# @lc code=start
class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    def findMaxConsecutiveOnes(self, nums):
        """
        use `one` to record the length of continuous ones
        use `two` to record two continuous ones separated by a single zero

        iterate through nums
        
            if n == 1: both add one
                one += 1
                two += 1
            else:
                reset two into one + 1
                then reset one to zero
                two = one + 1
                one = 0
        """
        res = two = one = 0
        for n in nums:
            if n == 0:
                two = one + 1
                one = 0
            else:
                one += 1
                two += 1
            res = max(res, two)
        return res
# @lc code=end
