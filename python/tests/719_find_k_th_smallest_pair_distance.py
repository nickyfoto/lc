#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (30.53%)
# Likes:    773
# Dislikes: 28
# Total Accepted:    28.2K
# Total Submissions: 91.6K
# Testcase Example:  '[1,3,1]\n1'
#
# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B. 
# 
# Example 1:
# 
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0 
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# 
# 
# 
# Note:
# 
# 2 .
# 0 .
# 1 .
# 
# 
#

# @lc code=start
class Solution:
    # def smallestDistancePair(self, nums: List[int], k: int) -> int:
    def smallestDistancePair(self, nums, k):
        def possible(mid):
            ctn = l = 0
            for r, num in enumerate(nums):
                while num - nums[l] > mid:
                    l += 1
                ctn += r - l
            return ctn >= k
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l

# @lc code=end
