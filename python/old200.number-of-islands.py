#
# @lc app=leetcode id=200 lang=python3
from itertools import count

class UF:
    
    def __init__(self, total):
        self.arr = list(range(total))
        self.count = total

    def find(self, p):
        while p != self.arr[p]:
            p = self.arr[p]
        return p
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        # print(p, q, rootP, rootQ)
        if rootP == rootQ:
            return
        self.arr[rootP] = rootQ
        self.count -= 1




class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        if not grid:
            return 0
        c = count()
        n_rows = len(grid)
        n_cols = len(grid[0])
        d = {}
        for r in range(n_rows):
            for j in range(n_cols):
                if grid[r][j] == '1':
                    d[(r,j)] = next(c)
        # print(d)
        # l = len(d)

        def valid(n):
            r, c = n
            return r >= 0 and r <= n_rows and c >= 0 and c <= n_cols

        def get_neighbors(k):
            r, c = k
            res = []
            up    = r - 1, c
            down  = r + 1, c
            left  = r, c - 1
            right = r, c + 1
            return [n for n in [up, down, left, right] if valid(n)]

        if len(d) == 0:
            return 0
        if len(d) == 1:
            return 1
        uf = UF(len(d))
        for k, v in d.items():
            for neighbor in get_neighbors(k):
                if neighbor in d:
                    uf.union(d[k], d[neighbor])

        return uf.count





# s = Solution()
# grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# print(s.numIslands(grid))


# grid = ["11000", "11000", "00100", "00011"]

# print(s.numIslands(grid))




















