#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (34.37%)
# Likes:    351
# Dislikes: 8
# Total Accepted:    12.2K
# Total Submissions: 30.2K
# Testcase Example:  '[8,2,4,7]\r\n4\r'
#
# Given an array of integers nums and an integer limit, return the size of the
# longest continuous subarray such that the absolute difference between any two
# elements is less than or equal to limit.
# 
# In case there is no subarray satisfying the given condition return 0.
# 
# 
# Example 1:
# 
# 
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute
# diff is |2-7| = 5 <= 5.
# 
# 
# Example 3:
# 
# 
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
# 
#

# @lc code=start
from sortedcontainers import SortedSet
class Solution:
    def longestSubarray(self, nums, limit):
        """
        using two deques
        """
        max_window = []
        min_window = []
        i = 0
        for num in nums:
            while len(max_window) and num > max_window[-1]:
                max_window.pop()
            while len(min_window) and num < min_window[-1]:
                min_window.pop()
            max_window.append(num)
            min_window.append(num)
            if max_window[0] - min_window[0] > limit:
                if max_window[0] == nums[i]:
                    max_window.pop(0)
                if min_window[0] == nums[i]:
                    min_window.pop(0)
                i += 1
        return len(nums) - i

    def longestSubarray(self, nums, limit):
        ss = SortedSet(key=lambda x: nums[x])
        ss.add(0)
        l = 0
        res = 1
        for r in range(1, len(nums)):
            ss.add(r)
            while nums[ss[-1]] - nums[ss[0]] > limit:
                ss.remove(l)
                l += 1
            res = max(res, r - l + 1)
        return res
# @lc code=end
