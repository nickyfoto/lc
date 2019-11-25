#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (30.12%)
# Total Accepted:    72.6K
# Total Submissions: 239.7K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means . 
# 
# 
#
class Solution:
    # def findUnsortedSubarray(self, nums: List[int]) -> int:
    def findUnsortedSubarray(self, nums):
        # there's a subarray that 
        n = len(nums)
        left, right = None, None
        for i in range(n-1):
            if nums[i+1] < nums[i]:
                left = i
                break
        # print(left)
        if left == None:
            return 0

        for i in range(n-1, -1, -1):
            if nums[i-1] > nums[i]:
                right = i
                break
        if right == None:
            return 0

        high = max(nums[:right])
        low = min(nums[left:])
        # low = min(nums)
        # print(high, low, right)

        left_small = n
        for i in range(right-1):
            if nums[i] > low:
                left_small = i
                break
        # print(left)
        while right < n and nums[right] < high:
            right += 1
        # print(left, left_small, right)
        return right-min(left, left_small)


# s = Solution()
# nums = [2, 6, 4, 8, 10, 9, 15]
# print(s.findUnsortedSubarray(nums) == 5)
# nums = [1,2,3,4]
# print(s.findUnsortedSubarray(nums) == 0)
# nums = [2,1]
# print(s.findUnsortedSubarray(nums) == 2)

# nums = [1,3,2,2,2]
# print(s.findUnsortedSubarray(nums) == 4)

# nums = [2,3,3,2,4]
# print(s.findUnsortedSubarray(nums) == 3)

# nums = [1,2,4,5,3]
# print(s.findUnsortedSubarray(nums) == 3)

# nums = [3,2,3,2,4]
# print(s.findUnsortedSubarray(nums) == 4)

# nums = [1,2,5,3,4]
# print(s.findUnsortedSubarray(nums) == 3)

# nums = [1,3,5,4,2]
# print(s.findUnsortedSubarray(nums) == 4)

# nums = [1,5,3,2,4]
# print(s.findUnsortedSubarray(nums) == 4)

# nums = [2,1,4,5,3]
# print(s.findUnsortedSubarray(nums) == 5)

# nums = [2,7,8,9,4,1,5,0,6,3]
# print(s.findUnsortedSubarray(nums) == 10)





