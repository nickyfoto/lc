#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#
# https://leetcode.com/problems/jump-game-v/description/
#
# algorithms
# Hard (55.28%)
# Likes:    90
# Dislikes: 5
# Total Accepted:    4K
# Total Submissions: 7.2K
# Testcase Example:  '[6,4,14,6,8,13,9,7,10,6,12]\n2'
#
# Given an array of integers arr and an integer d. In one step you can jump
# from index i to index:
# 
# 
# i + x where: i + x < arr.length and  0 < x <= d.
# i - x where: i - x >= 0 and  0 < x <= d.
# 
# 
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and
# arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) <
# k < max(i, j)).
# 
# You can choose any index of the array and start jumping. Return the maximum
# number of indices you can visit.
# 
# Notice that you can not jump outside of the array at any time.
# 
# 
# Example 1:
# 
# 
# Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# Output: 4
# Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as
# shown.
# Note that if you start at index 6 you can only jump to index 7. You cannot
# jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is
# between index 4 and 6 and 13 > 9.
# Similarly You cannot jump from index 3 to index 2 or index 1.
# 
# 
# Example 2:
# 
# 
# Input: arr = [3,3,3,3,3], d = 3
# Output: 1
# Explanation: You can start at any index. You always cannot jump to any
# index.
# 
# 
# Example 3:
# 
# 
# Input: arr = [7,6,5,4,3,2,1], d = 1
# Output: 7
# Explanation: Start at index 0. You can visit all the indicies. 
# 
# 
# Example 4:
# 
# 
# Input: arr = [7,1,7,1,7,1], d = 2
# Output: 2
# 
# 
# Example 5:
# 
# 
# Input: arr = [66], d = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 10^5
# 1 <= d <= arr.length
# 
#

# @lc code=start
class Solution:
    # def maxJumps(self, arr: List[int], d: int) -> int:
    # def maxJumps_wrong(self, arr, d):
        
    #     n = len(arr)

    #     def get_left(l, idx):
    #         res = 0
    #         for i in range(idx - 1, l - 1, -1):
    #             # print('get_left, i=', i)
    #             if arr[i] < arr[idx]:
    #                 # res += recur(i)
    #                 res += 1
    #             else:
    #                 return res
    #         return res
        
    #     def get_right(r, idx):
    #         res = 0
    #         for i in range(idx + 1, r + 1):
    #             # print('get_right, i=', i, arr[i], arr[i+1])
    #             if arr[idx] > arr[i]:
    #                 # res += recur(i)
    #                 res += 1
    #                 # print('res=', res)
    #             else:
    #                 # print('res=', res)
    #                 return res
    #         return res


    #     mx = 0
    #     memo = {}
    #     def recur(idx):
    #         print('check idx=', idx)
    #         if idx in memo:
    #             print('idx=', idx, 'memo =', memo[idx])
    #             return memo[idx]
    #         l = max(0, idx - d)
    #         r = min(idx + d, n - 1)
    #         print('l=', l, 'r=', r)
    #         left = get_left(l, idx)
    #         right = get_right(r, idx)
    #         memo[idx] = 1 + max(left, right)
    #         print('idx=', idx, 'res=', memo[idx])
    #         return memo[idx]
    #         # recur(idx + 1, memo)

    #     for i in range(n):
    #         mx = max(mx, recur(i))
    #     return mx

    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [0] * n
        res = 1

        def dfs(i):
            if dp[i] != 0: return dp[i]
            res = 1
            j = i + 1
            while j <= min(i + d, n - 1) and arr[j] < arr[i]:
                res = max(res, 1 + dfs(j))
                j += 1
            j = i - 1
            while j >= max(i - d, 0) and arr[j] < arr[i]:
                res = max(res, 1 + dfs(j))
                j -= 1
            dp[i] = res
            return res


        for i in range(n):
            res = max(res, dfs(i))
        return res
# @lc code=end
