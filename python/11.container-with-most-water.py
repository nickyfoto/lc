#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (46.35%)
# Total Accepted:    437.8K
# Total Submissions: 942.2K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution:
    # def maxArea(self, height: List[int]) -> int:
    def maxArea2(self, height) -> int:

        n = len(height)
        mx = - float('inf')
        mh = - float('inf')
        for i in range(n-1):
            mh = max(mh, height[i])
            if height[i] < mh:
                continue
            else:
                for j in range(i+1, n):
                    a = (j-i) * min(height[i], height[j])
                    mx = max(a, mx)

        # print(mx)
        return mx

    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        mx = - float('inf')
        while left != right:
            area = (right-left) * min(height[left], height[right])
            mx = max(mx, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return mx

# s = Solution()
# height = [1,8,6,2,5,4,8,3,7]
# print(s.maxArea(height))


















        
