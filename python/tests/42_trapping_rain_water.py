#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (46.52%)
# Likes:    5466
# Dislikes: 104
# Total Accepted:    420.2K
# Total Submissions: 902.4K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#

# @lc code=start
class Solution:
    # def trap(self, height: List[int]) -> int:
    def trap_v1(self, height):
        """
        calculate level by level
        for every element in height
        if idx is not 0 or n - 1
        count dist left and right is not zero, add to res
        all non-zero element - 1, recur
        v1 TLE
        """
        if len(height) < 3:
            return 0
        
        self.res = 0

        def recur(height):
            # print(len(height))
            if sum(height) < 2:
                return
            l = 0
            r = len(height) - 1
            while height[l] == 0:
                l += 1
            while height[r] == 0:
                r -= 1
            if l < r:
                height = height[l:r+1]
                self.res += height.count(0)
                recur([x - 1 if x > 0 else 0 for x in height])
            else:
                return

        recur(height)
        return self.res

    def trap(self, height):
        
        if len(height) < 3 or sum(height) < 2:
            return 0
        
        self.res = 0

        def recur(l, r):
            # print(l, r)
            # print(self.res)    
            if l >= r:
                return
            self.res += height[l:r+1].count(0)
            # print(self.res)
            height[l:r+1] = [x - 1 if x > 0 else 0 for x in height[l:r+1]]
            
            while l < r and height[l] == 0:
                l += 1
            while r > l and height[r] == 0:
                r -= 1
            if l < r:
                recur(l, r)
            return
        
        sh = [x for x in sorted(list(set(height)))]
        if sh[0] != 0:
            sh = [0] + sh

        l = 0
        r = len(height) - 1
        while height[l] == 0:
            l += 1
        while height[r] == 0:
            r -= 1
        # print(l, r, sh)
        for i in range(1, len(sh)):
            h = sh[i] - sh[i-1]
            # print(h)
            self.res += height[l:r+1].count(0) * h
            # print(self.res, l, r)
            height[l:r+1] = [x - h if x > 0 else 0 for x in height[l:r+1]]
            while l < r and height[l] == 0:
                l += 1
            while r > l and height[r] == 0:
                r -= 1
            if l >= r:
                break
        # if l < r:
            # recur(l, r)
        return self.res
# @lc code=end
