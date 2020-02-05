#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (33.09%)
# Likes:    2948
# Dislikes: 264
# Total Accepted:    354.8K
# Total Submissions: 1.1M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#

# @lc code=start
class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    def canJump_me(self, nums) -> bool:
        """
        first check whether it can directly reach last, if yes return True
        if not, whther it can reach other nodes that can reach last, if yes return True
        if not, whether it can reach other nodes that can reach ...
        """
        n = len(nums)
        
        def recur(startIdx):
            # print('startIdx =', startIdx)
            if startIdx + nums[startIdx] >= n - 1:
                return True
            else:
                dist = startIdx + nums[startIdx]
                nextIdx = startIdx
                # print(startIdx, startIdx + nums[startIdx])
                for i in range(startIdx, startIdx + nums[startIdx] + 1):
                    if i + nums[i] > dist:
                        dist = i + nums[i]
                        nextIdx = i
                # print(nextIdx, dist)
                if dist == startIdx + nums[startIdx]:
                    return False
                return recur(nextIdx)

        return recur(0)


    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0

# @lc code=end
