#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.44%)
# Total Accepted:    12.6K
# Total Submissions: 27.2K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
#
class Solution:
    # def orangesRotting(self, grid: List[List[int]]) -> int:
    def orangesRotting(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])
        days = [[0]*n_cols for c in [0]*n_rows]


        def getUp(r, c, path):
            if r < 0 or grid[r][c] == 0 or (r, c) in path:
                return None
            path.append((r, c))
            return (r,c), grid[r][c]
        def getDown(r, c, path):
            if r >= n_rows or grid[r][c] == 0 or (r, c) in path:
                return None
            path.append((r,c))
            return (r,c), grid[r][c]
        def getLeft(r, c, path):
            # print('getLeft', r, c, path)
            if c < 0 or grid[r][c] == 0 or (r,c) in path:
                return None
            path.append((r,c))
            # print('here')
            return (r,c), grid[r][c]
        def getRight(r, c, path):
            if c >= n_cols or grid[r][c] == 0 or (r,c) in path:
                return None
            path.append((r,c))
            return (r,c), grid[r][c]

        class TreeNode:
            def __init__(self, r, c, path):
                # print(r, c)
                self.val = grid[r][c]
                self.path = path
                self.up = getUp(r-1, c, self.path)
                self.down = getDown(r+1, c, self.path)
                self.left = getLeft(r,c-1, self.path)
                self.right = getRight(r,c+1, self.path)


        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    path = [(r, c)]
                    q = []
                    node = TreeNode(r, c, path)
                    # dist = 1
                    found = False
                    q.append((node, 1))
                    while not found and q:
                        n, dist = q.pop(0)
                        # print(r,c,[n.up, n.down, n.left, n.right])
                        # print('q=', q)
                        for val in [n.up, n.down, n.left, n.right]:
                            if val:
                                if val[1] == 2:
                                    # print('here')
                                    days[r][c] = dist
                                    found = True
                                    break
                                else:
                                    q.append((TreeNode(*val[0], path), dist+1))
                        # print(q)
        # print(grid)
        # print('days=', days)
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1 and days[r][c] == 0:
                    return -1
        from functools import reduce
        return max(reduce(lambda x, y: x+y, days))

        


# s = Solution()

# grid = [[2,1,1],[1,1,0],[0,1,1]]
# print(s.orangesRotting(grid))



# grid = [[2,1,1],[0,1,1],[1,0,1]]
# print(s.orangesRotting(grid))




# grid = [[0,2]]
# print(s.orangesRotting(grid))


# grid = [[1,2]]
# print(s.orangesRotting(grid))



















        
