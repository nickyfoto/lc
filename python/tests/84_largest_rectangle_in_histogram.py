#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (33.41%)
# Likes:    2829
# Dislikes: 68
# Total Accepted:    223.5K
# Total Submissions: 669K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#

# @lc code=start
class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    def largestRectangleArea_forum(self, heights):
        """
        the answer must be some area that contains the a whole bar
        and the max area for each bar is equal to the width * heights[i]
        width = right - left - 1
        right is the rightside idx of the first bar has height less than heights[i]
        left is the leftside idx of the first bar has height less than heights[i]

        the probem becomes to efficiently find left, right for each height[i]
        we save these information on two array called left and right
        """
        if not heights:
            return 0
        n = len(heights)
        mx = heights[0]
        left = [0] * n
        right = [0] * n
        left[0] = -1
        right[-1] = n

        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p
        
        for i in range(n - 1)[::-1]:
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p

        for i, h in enumerate(heights):
            mx = max(mx, h * (right[i] - left[i] - 1))
        return mx

    def largestRectangleArea(self, heights):
        heights.append(0)
        mx = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                mx = max(mx, h * w)
            stack.append(i)
        return mx
# @lc code=end
