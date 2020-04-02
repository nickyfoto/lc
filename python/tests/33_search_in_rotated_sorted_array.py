#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.58%)
# Likes:    3629
# Dislikes: 396
# Total Accepted:    560.9K
# Total Submissions: 1.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
from bisect import bisect_left
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search_me(self, nums, target):
        if not nums:
            return -1

        def bs(nums, target):
            b = bisect_left(nums, target)
            # print('here', nums, b)
            if b == len(nums) or nums[b] != target:
                return -1
            return b


        def find_k(nums):
            if nums[0] < nums[-1]:
                return 0
            # print('nums=', nums)
            if len(nums) > 1:
                mid = len(nums) // 2
                # print(nums, nums[mid], 'mid=', mid)
                if nums[mid-1] > nums[mid]:
                    return mid
                else:
                    if nums[0] > nums[mid]:
                        return find_k(nums[:mid])
                    else:
                        # print('here')
                        return mid + find_k(nums[mid:])
            else:
                return 0
        
        # nums = [1,2,4,5,6,7,0]
        # print(find_k(nums) == 6) 
        # nums = [2,4,5,6,7,0,1]
        # print(find_k(nums) == 5) 
        # nums = [4,5,6,7,0,1,2]
        # print(find_k(nums) == 4)    
        # nums = [5,6,7,0,1,2,4]
        # print(find_k(nums) == 3) 
        # nums = [6,7,0,1,2,4,5]
        # print(find_k(nums) == 2)   
        # nums = [7,0,1,2,4,5,6]
        # print(find_k(nums) == 1)   
        # nums = [0,1,2,4,5,6,7]
        # print(find_k(nums) == 0)  



        k = find_k(nums)
        # print('k=', k)
        if target == nums[k]:
            return k
        else:
            if k == 0 and nums[0] <= target <= nums[-1]:
                return bs(nums, target)
            elif k == len(nums) - 1 and nums[0] <= target <= nums[k-1]:
                return bs(nums[:-1], target)
            else:
                if nums[0] <= target <= nums[k-1]:
                    return bs(nums[:k], target)
                elif nums[k] < target <= nums[-1]:
                    b = bs(nums[k:], target)
                    # print('here', b)
                    if b != -1:
                        return k + b
                    return -1
                else:
                    return -1
        
            


        # return find_k(nums)

    def search(self, nums, target):
        """
        not undertand yet
        https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple/187360
        """
        l, h = 0, len(nums)
        while l < h:
            mid = (l + h) // 2
            num = nums[mid]
            if (num < nums[0]) == (target < nums[0]):
                if target < num:
                    h = mid
                elif target > num:
                    l = mid + 1
                else:
                    return mid
            elif target < nums[0]:
                l = mid + 1
            else:
                h = mid
        return -1

    def search(self, nums, target):
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res = mid
                break
            elif nums[l] <= nums[mid]: # use <= because l can be equal to mid
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return res
# @lc code=end
