#
# @lc app=leetcode id=1102 lang=python3
#
# [1102] Path With Maximum Minimum Value
#
# https://leetcode.com/problems/path-with-maximum-minimum-value/description/
#
# algorithms
# Medium (49.00%)
# Likes:    331
# Dislikes: 36
# Total Accepted:    13.4K
# Total Submissions: 27.3K
# Testcase Example:  '[[5,4,5],[1,2,6],[7,4,6]]'
#
# Given a matrix of integers A with R rows and C columns, find the maximum
# score of a path starting at [0,0] and ending at [R-1,C-1].
# 
# The score of a path is the minimum value in that path.  For example, the
# value of the path 8 →  4 →  5 →  9 is 4.
# 
# A path moves some number of times from one visited cell to any neighbouring
# unvisited cell in one of the 4 cardinal directions (north, east, west,
# south).
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[5,4,5],[1,2,6],[7,4,6]]
# Output: 4
# Explanation: 
# The path with the maximum score is highlighted in yellow. 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
# Output: 2
# 
# Example 3:
# 
# 
# 
# 
# Input:
# [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
# Output: 3
# 
# 
# 
# Note:
# 
# 
# 1 <= R, C <= 100
# 0 <= A[i][j] <= 10^9
# 
# 
#

# @lc code=start
import math
from pprint import pprint
class Solution:
    # def maximumMinimumPath(self, A: List[List[int]]) -> int:
    def maximumMinimumPath(self, A):
        if A[0][0] == 0 or A[-1][-1] == 0: return 0
        mx = max(A[0][0], A[-1][-1])
        if mx == 0: return 0
        m, n = len(A), len(A[0])
        mn = math.inf
        s = set()
        for i in range(m):
            for j in range(n):
                mn = min(mn, A[i][j])
                s.add(A[i][j])
        if mn == mx: return mn
        vals = list(s)
        vals.sort()
        def connected(arr):
            if arr[0][0] != 1:
                return False
            q = [[(0, 0)]]
            vis = {(0, 0): True}

            def get_nodes(i, j):
                up = i - 1, j
                down = i + 1, j
                left = i, j - 1
                right = i, j + 1
                res = []
                for i, j in [up, down, left, right]:
                    if 0 <= i < m and 0 <= j < n and (i, j) not in vis and arr[i][j] == 1:
                        vis[i, j] = True
                        res.append((i, j))
                return res
            
            def bfs():
                while q:
                    nodes = q.pop(0)
                    new_nodes = []
                    for i, j in nodes:
                        if (i, j) == (m - 1, n - 1):
                            return True
                        neighbors = get_nodes(i, j)
                        new_nodes.extend(neighbors)
                    if new_nodes:
                        q.append(new_nodes)
                return False
            # return bfs()

            def dfs():
                q = [(0, 0)]
                while q:
                    i, j = q.pop()
                    for i, j in get_nodes(i, j):
                        if (i, j) == (m - 1, n - 1):
                            return True
                        vis[i, j] = True
                        q.append((i, j))
                return False
            return dfs()


        def has_path(mid):
            arr = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if mid <= A[i][j]:
                        arr[i][j] = 1
            # print('val=', mid)
            # pprint(arr)
            if connected(arr):
                return True
            return False
        
        # print(vals)
        l, r = 0, len(vals) - 1
        while l <= r:
            # print(vals)
            mid = l + (r - l) // 2
            # print('mid=', mid, vals[mid], has_path(vals[mid]))
            if has_path(vals[mid]):
                l = mid + 1
            else:
                r = mid - 1
        # print(l, r, mid)
        return vals[r]
# @lc code=end
