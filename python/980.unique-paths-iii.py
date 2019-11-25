#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (71.55%)
# Total Accepted:    16.4K
# Total Submissions: 23K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# On a 2-dimensional grid, there are 4 types of squares:
# 
# 
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# 
# 
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# 
# 
# Example 2:
# 
# 
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# 
# 
# Example 3:
# 
# 
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length * grid[0].length <= 20
# 
#
from collections import defaultdict, OrderedDict

class Solution:
    # def uniquePathsIII(self, grid: List[List[int]]) -> int:
    def uniquePathsIII(self, grid) -> int:


        n_rows = len(grid)
        n_cols = len(grid[1])

        # if n_rows == 1 or n_cols == 1:
            # return 1
        obs = defaultdict(lambda: False)
        n_obs = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    s = (r,c)
                elif grid[r][c] == 2:
                    e = (r,c)
                elif grid[r][c] == -1:
                    obs[(r,c)] = True
                    n_obs += 1
        
        # print(s, e, n_obs)
        
        target = n_rows * n_cols - 1 - n_obs


        

        def get_neighbors(node, path):

            def valid(point):
                r, c = point
                return n_rows > r >= 0 and n_cols > c >= 0 and not obs[(r,c)] and (r,c) not in path

            r,c = node
            up    = r - 1, c
            down  = r + 1,c
            left  = r, c - 1
            right = r, c + 1
            return filter(valid, [up, down, left, right])


        ctn = 0

        stack = [OrderedDict({s: None})]
        while stack:
            path = stack.pop()
            node, _ = path.popitem()
            path[node] = None
            # print(node, path)
            neighbors = get_neighbors(node, path)
            for n in neighbors:
                if n == e:
                    # print(path.keys())
                    if len(path) == target:
                        ctn += 1
                    # todo

                else:
                    # print('here', n)
                    pc = path.copy()
                    pc[n] = None
                    stack.append(pc)
        return ctn

s = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(s.uniquePathsIII(grid))



grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(s.uniquePathsIII(grid))



grid = [[0,1],[2,0]]
print(s.uniquePathsIII(grid))














        
