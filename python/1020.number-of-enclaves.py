#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
# https://leetcode.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (54.76%)
# Total Accepted:    9.5K
# Total Submissions: 17.4K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# Given a 2D array A, each cell is 0 (representing sea) or 1 (representing
# land)
# 
# A move consists of walking from one land square 4-directionally to another
# land square, or off the boundary of the grid.
# 
# Return the number of land squares in the grid for which we cannot walk off
# the boundary of the grid in any number of moves.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: 
# There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed
# because its on the boundary.
# 
# Example 2:
# 
# 
# Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: 
# All 1s are either on the boundary or can reach the boundary.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 500
# 1 <= A[i].length <= 500
# 0 <= A[i][j] <= 1
# All rows have the same size.
# 
#
from collections import defaultdict
class Solution:
    # def numEnclaves(self, A: List[List[int]]) -> int:
    def numEnclaves(self, A):



        n_rows = len(A)
        n_cols = len(A[0])


        explored = defaultdict(lambda: False)


        def touch_boundary(point):
            r, c = point
            return r == 0 or r == n_rows-1 or c == 0 or c == n_cols - 1

        class Node:
            
            def __init__(self, point, boundary):
                self.r, self.c = point
                self.count = 1
                self.boundary = boundary

            def valid(self, point):
                r, c = point
                return r >= 0 and r < n_rows and c >= 0 and c < n_cols and A[point[0]][point[1]] and not explored[point]

            def _dfs(self, point):
                # print(point)
                if not self.valid(point):
                    return self.boundary, 0
                if touch_boundary(point):
                    self.boundary = True
                
                explored[point] = True
                node = Node(point, self.boundary)
                self.boundary, count = node.dfs()
                return self.boundary, count
                    
            def dfs(self):
                up = self.r - 1, self.c
                self.boundary, count = self._dfs(up)
                self.count += count
                down = self.r + 1, self.c
                self.boundary, count = self._dfs(down)
                self.count += count
                # print('starting point=', point, self.boundary, count, self.count)
                left = self.r, self.c-1
                self.boundary, count = self._dfs(left)
                self.count += count
                right = self.r, self.c+1
                self.boundary, count = self._dfs(right)
                self.count += count
                if not self.boundary:
                    return self.boundary, self.count
                else:
                    return self.boundary, 0

        res = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if A[r][c] == 1:
                    point = r, c
                    if not explored[point]:
                        explored[point] = True
                        node = Node(point, touch_boundary(point))
                        _, count = node.dfs()
                        # print(point, count)
                        res += count
        return res

# s = Solution()
# A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# print(s.numEnclaves(A))




# A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# print(s.numEnclaves(A))

# A = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
# print(s.numEnclaves(A))












        
