#
# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#
# https://leetcode.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (62.92%)
# Total Accepted:    8.4K
# Total Submissions: 13.5K
# Testcase Example:  '[" /","/ "]'
#
# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /,
# \, or blank space.  These characters divide the square into contiguous
# regions.
# 
# (Note that backslash characters are escaped, so a \ is represented as "\\".)
# 
# Return the number of regions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input:
# [
# " /",
# "/ "
# ]
# Output: 2
# Explanation: The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# [
# " /",
# "  "
# ]
# Output: 1
# Explanation: The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 3:
# 
# 
# Input:
# [
# "\\/",
# "/\\"
# ]
# Output: 4
# Explanation: (Recall that because \ characters are escaped, "\\/" refers to
# \/, and "/\\" refers to /\.)
# The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 4:
# 
# 
# Input:
# [
# "/\\",
# "\\/"
# ]
# Output: 5
# Explanation: (Recall that because \ characters are escaped, "/\\" refers to
# /\, and "\\/" refers to \/.)
# The 2x2 grid is as follows:
# 
# 
# 
# 
# Example 5:
# 
# 
# Input:
# [
# "//",
# "/ "
# ]
# Output: 3
# Explanation: The 2x2 grid is as follows:
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] is either '/', '\', or ' '.
# 
# 
# 
# 
# 
# 
#
class CELL:
    def __init__(self, row, col, cut):
        self.row = row
        self.col = col
        self.cut = cut

class UF:
    def __init__(self, total, n):
        self.arr = list(range(total))
        self.count = total
        self.n = n
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
    def union_empty(self, lst):
        for i in range(len(lst)-1):
            self.union(lst[i], lst[i+1])
    
    def union_f_slash(self, lst):
        self.union(lst[0], lst[1])
        self.union(lst[2], lst[3])

    def union_b_slash(self, lst):
        self.union(lst[0], lst[3])
        self.union(lst[1], lst[2])
    
    def union_left(self, c):
        start = (4*self.n) * c.row + 4 * c.col
        params = range(start, start+4)
        own = params[0]
        # print(params[0], self.arr)
        left = (4*self.n) * c.row + 4 * (c.col-1)
        left_params = range(left, left+4)
        left = left_params[2]
        # print(left, own)
        self.union(self.arr[own], self.arr[left])
        # print(self.arr, self.count)

    def union_up(self, c):
        start = (4*self.n) * c.row + 4 * c.col
        params = range(start, start+4)
        own = params[1]
        # print('here', own)
        up = (4*self.n) * (c.row-1) + 4 * c.col
        up_params = range(up, up+4)
        up = up_params[3]
        self.union(self.arr[own], self.arr[up])
    def union_adj(self, c):
        if c.row > 0:
            self.union_up(c)
        if c.col > 0:
            self.union_left(c)
    
    def process(self, c):
        # print(c)
        start = (4*self.n)*c.row+4*c.col
        params = range(start, start+4)
        if c.cut == " ":
            # print('here', start, params)
            self.union_empty(params)
        elif c.cut == '/':
            self.union_f_slash(params)
        elif c.cut == '\\':
            self.union_b_slash(params)
        self.union_adj(c)

class Solution:
    # def regionsBySlashes(self, grid: List[str]) -> int:
    def regionsBySlashes(self, grid):
        n = len(grid)
        # print(n, len(grid[0]))
        # print(grid)
        total = n**2 * 4
        # total cells
        # print(total)
        uf = UF(total, n)
        # print(uf.count)
        for i in range(n):
            for j in range(n):
                cell = CELL(i, j, grid[i][j])
                # print(grid[i][j])
                uf.process(cell)
                # print(uf.count, uf.arr)
        return uf.count
# print(len("\\"))
# print("\\")



# s = Solution()
# grid = [
# " /",
# "/ "
# ]
# print(s.regionsBySlashes(grid)==2)
# grid = [
#   " /",
#   "  "
# ]
# print(s.regionsBySlashes(grid)==1)
# grid = [
#   "\\/",
#   "/\\"
# ]
# print(s.regionsBySlashes(grid)==4)
# grid = [
#   "/\\",
#   "\\/"
# ]
# print(s.regionsBySlashes(grid)==5)
# grid = [
#   "//",
#   "/ "
# ]
# print(s.regionsBySlashes(grid)==3)

# grid = [' /\\', ' \\/', '\\  ']
# print(s.regionsBySlashes(grid) == 4)
