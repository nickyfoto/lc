#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#
# https://leetcode.com/problems/number-of-islands-ii/description/
#
# algorithms
# Hard (40.47%)
# Likes:    745
# Dislikes: 18
# Total Accepted:    70.2K
# Total Submissions: 174.2K
# Testcase Example:  '3\n3\n[[0,0],[0,1],[1,2],[2,1]]'
#
# A 2d grid map of m rows and n columns is initially filled with water. We may
# perform an addLand operation which turns the water at position (row, col)
# into a land. Given a list of positions to operate, count the number of
# islands after each addLand operation. An island is surrounded by water and is
# formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
# 
# Example:
# 
# 
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# 
# 
# Explanation:
# 
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water
# and 1 represents land).
# 
# 
# 0 0 0
# 0 0 0
# 0 0 0
# 
# 
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 
# 
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 
# 
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# 
# 
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# 
# 
# Follow up:
# 
# Can you do it in time complexity O(k log mn), where k is the length of the
# positions?
# 
#

# @lc code=start
class UF:
    
    def __init__(self):
        self.arr = {}
        self.rank = {}
        self.ctn = 0

    def find_opt(self, p):
        """
        path compression
        """
        if p != self.arr[p]:
            self.arr[p] = self.find_opt(self.arr[p])
        return self.arr[p]
    
    def union(self, sm, lg):
        """
        sm: small, lg: large
        """
        rs = self.find_opt(sm)
        rl = self.find_opt(lg)
        if rs != rl:
            if self.rank[rs] < self.rank[rl]:
                rs, rl = rl, rs
            self.arr[rl] = rs
            self.rank[rs] += self.rank[rl] == self.rank[rs]
            self.ctn -= 1

class Solution:
    # def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    def numIslands2(self, m, n, positions):
        uf = UF()
        res = []
        for i, j in positions:
            x = i, j
            if x in uf.arr:
                res.append(res[-1])
                continue
            uf.arr[x] = x
            uf.rank[x] = 1
            uf.ctn += 1
            for y in (i - 1, j), ( i + 1, j), (i, j - 1), (i, j + 1):
                if y in uf.arr:
                    uf.union(x, y)
            res.append(uf.ctn)
        return res
        
# @lc code=end
