#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#
# https://leetcode.com/problems/path-with-maximum-gold/description/
#
# algorithms
# Medium (60.36%)
# Total Accepted:    6.3K
# Total Submissions: 10.4K
# Testcase Example:  '[[0,6,0],[5,8,7],[0,9,0]]'
#
# In a gold mine grid of size m * n, each cell in this mine has an integer
# representing the amount of gold in that cell, 0 if it is empty.
# 
# Return the maximum amount of gold you can collect under the conditions:
# 
# 
# Every time you are located in a cell you will collect all the gold in that
# cell.
# From your position you can walk one step to the left, right, up or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has
# some gold.
# 
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
# ⁠[5,8,7],
# ⁠[0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
# ⁠[2,0,6],
# ⁠[3,4,5],
# ⁠[0,3,0],
# ⁠[9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length, grid[i].length <= 15
# 0 <= grid[i][j] <= 100
# There are at most 25 cells containing gold.
# 
#
class Solution:
    # def getMaximumGold(self, grid: List[List[int]]) -> int:
    def getMaximumGold(self, grid):

        n_rows = len(grid)
        n_cols = len(grid[0])

        class Node:
            def __init__(self, r,c):
                self.r = r
                self.c = c
                self.gold = 0
            
            def neighbors(self, node, visited):

                def valid(point):
                    r,c = point
                    return n_rows > r >= 0 and n_cols > c >= 0 and point not in visited and grid[r][c] != 0

                r, c = node
                up    = r - 1, c 
                down  = r + 1, c
                left  = r, c - 1
                right = r, c + 1
                return filter(valid, [up, down, left, right])

            def collect(self):
                start = (self.r, self.c)
                g = grid[self.r][self.c]
                visited = {start: None, 'last': start, 'gold': g}
                stack = [visited]
                while stack:
                    visited = stack.pop()
                    node = visited['last']
                    neighbors = list(self.neighbors(node, visited))
                    # print(node, neighbors)
                    if neighbors:
                        for n in neighbors:
                            vc = visited.copy()
                            vc[n] = None
                            vc['last'] = n
                            vc['gold'] += grid[n[0]][n[1]]
                            stack.append(vc)
                        # print(stack)
                    else:
                        self.gold = max(self.gold, visited['gold'])
                        # del visited['last']
                        # self.gold = max(self.gold, sum( grid[r][c] for r,c in visited.keys() ))
                        # self.path_length = max(self.path_length, len(path))
                        # print(path)
                        # todo



        res = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] != 0:
                    node = Node(r,c)
                    node.collect()
                    res = max(node.gold, res)
                    # print(node.path_length)
                    # if node.path_length == 25:
                        # return res
        return res


import time

start = time.time()


s = Solution()
# grid = [[0,6,0],[5,8,7],[0,9,0]]
# print(s.getMaximumGold(grid))


# grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# print(s.getMaximumGold(grid))


grid = [[5,3,36,26,27],
        [11,31,23,30,4],
        [5,7,21,38,10],
        [39,30,10,17,13],
        [16,0,0,26,1],
        [25,0,10,0,0]]
print(s.getMaximumGold(grid))

end = time.time()
print(end - start)