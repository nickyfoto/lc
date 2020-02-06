#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#
# https://leetcode.com/problems/jump-game-iii/description/
#
# algorithms
# Medium (61.11%)
# Likes:    155
# Dislikes: 3
# Total Accepted:    10.5K
# Total Submissions: 17.2K
# Testcase Example:  '[4,2,3,0,3,1,2]\n5'
#
# Given an array of non-negative integers arr, you are initially positioned at
# start index of the array. When you are at index i, you can jump to i + arr[i]
# or i - arr[i], check if you can reach to any index with value 0.
# 
# Notice that you can not jump outside of the array at any time.
# 
# 
# Example 1:
# 
# 
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# 
# 
# Example 2:
# 
# 
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# 
# 
# Example 3:
# 
# 
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length
# 
#

# @lc code=start
class Solution:
    # def canReach(self, arr: List[int], start: int) -> bool:
    def canReach_me(self, arr, start):
        total = {}
        n = len(arr)
        
        def recur(d):
            total.update(d)
            new = {}
            for i in d:
                if d[i] == 0:
                    return True
                l, r = i - arr[i], i + arr[i]
                if 0 <= l < n and l not in total:
                    new[l] = arr[l]
                if 0 <= r < n and r not in total:
                    new[r] = arr[r]
            if not new:
                return False
            return recur(new)
        d = {start: arr[start]}
        return recur(d)

    def canReach(self, arr, start):
        n = len(arr)
        if 0 <= start < n and arr[start] < n:
            jump = arr[start]
            arr[start] += n
            return jump == 0 or self.canReach(arr, start + jump) or self.canReach(arr, start - jump)
# @lc code=end
