#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (29.59%)
# Likes:    1844
# Dislikes: 107
# Total Accepted:    220.5K
# Total Submissions: 744.7K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#

# @lc code=start
class Solution:
    # def jump(self, nums: List[int]) -> int:
    def jump_v1(self, nums):
        """
        TLE on 91/92
        """
        n = len(nums)
        if n == 1:
            return 0
        def bfs(neighbors, steps):
            # print(neighbors)
            if n - 1 in neighbors:
                return steps
            new = {}
            for i in neighbors:
                new.update( {1 + i + d: nums[i + 1 + d] for d in range(nums[i]) if i + 1 + d < n} )
            return bfs(new, steps + 1)
        neighbors = {1 + d: nums[1 + d] for d in range(nums[0]) if 1 + d < n}
        # print(neighbors)
        return bfs(neighbors, 1)

    def jump_v2(self, nums):
        n = len(nums)
        l, r = 0, 0
        left_right = [l, l + 1]
        steps = 0
        while r < n - 1:
            for i in range(*left_right):
                if i < n:
                    r = max(r, i + nums[i])
                else:
                    break
            left_right = [l + 1, r + 1]
            l = r
            steps += 1
        return steps

    def jump(self, nums):
        """
        forum
        """
        steps = 0
        l = 0
        r = 0
        n = len(nums)
        for i in range(n - 1):
            r = max(r, i + nums[i])
            if i == l:
                steps += 1
                l = r
        return steps





# @lc code=end
