#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.61%)
# Total Accepted:    324.7K
# Total Submissions: 744.3K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#
class Solution:
    # def findMin(self, nums: List[int]) -> int:
    def findMin(self, nums) -> int:

        def recur(nums):
            # print('searching', nums)
            n = len(nums)
            if n == 1:
                return nums[0]
            if n % 2 == 1:
                mid = n // 2
            else:
                mid = n // 2 - 1

            # print(nums[mid], nums[0])

            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            else:
                if nums[0] > nums[mid] or nums[0] < nums[-1]:
                    return recur(nums[:mid])
                else:
                    return recur(nums[mid:])
                    


    

        return recur(nums)





# s = Solution()
# nums = [4,5,6,7,0,1,2]
# print(s.findMin(nums) == 0)

# nums = [3,4,5,1,2] 
# print(s.findMin(nums) == 1)


# nums = [4,1,2,3]
# print(s.findMin(nums) == 1)

# nums = [9,10,1,2,3,4,5,6,7,8]
# print(s.findMin(nums) == 1)


# nums = [3,4,5,6,7,8,9,10,1,2]
# print(s.findMin(nums) == 1)

# nums = list(range(10))
# print(s.findMin(nums) == 0)









        
