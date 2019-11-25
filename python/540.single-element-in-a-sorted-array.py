#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.48%)
# Total Accepted:    66.7K
# Total Submissions: 116.1K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# 
# 
# Note: Your solution should run in O(log n) time and O(1) space.
# 
#
class Solution:
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    def singleNonDuplicate2(self, nums):
        

        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(1, n,  2):
            # print(i, nums[i-1], nums[i])
            if nums[i-1] != nums[i]:
                return nums[i-1]
        else:
            return nums[-1]
            # if nums[i-1] != nums[i]


    def singleNonDuplicate(self, nums):

        n = len(nums)
        if n == 1:
            return nums[0]
        def recur(left, right):
            # print('left=', left, 'right=', right)
            if right == left:
                return nums[right]

            mid = left+(right - left) // 2
            if right - left == 2:
                if nums[mid] == nums[left]:
                    return nums[right]
                else:
                    return nums[left]
            else:
                if nums[mid] == nums[mid-1]:
                    if (right - mid) % 2 == 1:
                        return recur(mid+1, right)
                    else:
                        # print('left=', left, 'mid=', mid-2)
                        return recur(left, mid - 2)
                elif nums[mid] == nums[mid+1]:
                    if (right - (mid+1)) % 2 == 1:
                        return recur(mid+2, right)
                    else:
                        # print('left=', left, 'mid=', mid-2)
                        return recur(left, mid - 1)
                else:
                    return nums[mid]
        return recur(0, n - 1)



s = Solution()
nums = [1,1,2,3,3,4,4,8,8]
print(s.singleNonDuplicate(nums) == 2)


nums = [3,3,7,7,10,11,11]
print(s.singleNonDuplicate(nums) == 10)





nums = [1,1,2]
print(s.singleNonDuplicate(nums) == 2)




nums = [1,1,2,2,3,4,4,8,8]
print(s.singleNonDuplicate(nums) == 3)

nums = [1,1,2,2,3,3,4,4,8]
print(s.singleNonDuplicate(nums) == 8)


nums = [1,2,2,3,3,4,4,8,8]
print(s.singleNonDuplicate(nums) == 1)

nums = [1,1,2,2,3]
print(s.singleNonDuplicate(nums) == 3)