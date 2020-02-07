#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.56%)
# Likes:    4029
# Dislikes: 148
# Total Accepted:    536K
# Total Submissions: 1.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
# from lcpy import UF

class UF:
    
    def __init__(self, total):
        self.arr = list(range(total))
        self.num_of_roots = total

    def find(self, p):
        while p != self.arr[p]:
            p = self.arr[p]
        return p
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.arr[rootP] = rootQ
        self.num_of_roots -= 1

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        uf = UF(m * n)
        # print(uf.num_of_roots)
        def connect(r, c):
            # up
            if r - 1 >= 0 and grid[r - 1][c] == '1':
                uf.union(n * (r - 1) + c, n * r + c)
            # down
            if r + 1 < m and grid[r + 1][c] == '1':
                uf.union(n * (r + 1) + c, n * r + c)
            # left
            if c - 1 >= 0 and grid[r][c - 1] == '1':
                uf.union(n * r + c - 1, n * r + c)
            # right
            if c + 1 < n and grid[r][c + 1] == '1':
                uf.union(n * r + c + 1, n * r + c)

        num_zeros = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    connect(r, c)
                    # print(r, c, 'root=', uf.find(r * n + c))
                else:
                    num_zeros += 1

        return uf.num_of_roots - num_zeros

# @lc code=end
