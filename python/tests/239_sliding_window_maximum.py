#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (40.62%)
# Likes:    2520
# Dislikes: 148
# Total Accepted:    218.8K
# Total Submissions: 538.7K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
#

# @lc code=start
from bisect import bisect_left, insort_left
from collections import deque
class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
    def maxSlidingWindow(self, nums, k):
        """
        i = 0
            d = [0]
            res = []
        i = 1
            n = 3
            nums[d[-1]] = nums[0] < n
                d = []
            d = [1]
            res = []
        i = 2
            n = -1
            nums[d[-1]] = nums[1] > n
            d = [1,2]
            i >= k - 1
                res = [3]
        """
        d = deque()
        res = []
        for i, n in enumerate(nums):
            # make sure the rightmost >= n
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            # make sure the leftmost is within the sliding window
            if d[0] == i - k:
                d.popleft()
            # starting point where we add the largest val to res
            if i >= k - 1:
                res += nums[d[0]],
        return res



    def maxSlidingWindow_me(self, nums, k):
        if not nums:
            return []
        if k == 1:
            return nums
        arr = sorted(nums[:k])
        res = []
        res.append(arr[k - 1])
        for i in range(len(nums) - k):
            idx = bisect_left(arr, nums[i])
            if idx == k - 1:
                res.append(max(arr[k - 2], nums[i + k]))
            else:
                # print('arr=', arr, 'len(nums)=', len(nums), 'i+k=', i + k)
                res.append(max(arr[k - 1], nums[i + k]))
            # arr = arr[:idx] + arr[idx + 1:]
            del arr[idx]
            insort_left(arr, nums[i + k])
        return res
    
    
    
    def maxSlidingWindow_v1(self, nums, k):
        res = []
        # print()
        for i in range(len(nums) - k + 1):
            # print(nums[i:i+k])
            res.append(max(nums[i:i+k]))
        return res
# @lc code=end
