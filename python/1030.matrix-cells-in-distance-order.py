#
# @lc app=leetcode id=1030 lang=python3
#
# [1030] Matrix Cells in Distance Order
#
# https://leetcode.com/problems/matrix-cells-in-distance-order/description/
#
# algorithms
# Easy (65.33%)
# Total Accepted:    9.5K
# Total Submissions: 14.6K
# Testcase Example:  '1\n2\n0\n0'
#
# We are given a matrix with R rows and C columns has cells with integer
# coordinates (r, c), where 0 <= r < R and 0 <= c < C.
# 
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
# 
# Return the coordinates of all cells in the matrix, sorted by their distance
# from (r0, c0) from smallest distance to largest distance.  Here, the distance
# between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2|
# + |c1 - c2|.  (You may return the answer in any order that satisfies this
# condition.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: R = 1, C = 2, r0 = 0, c0 = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1]
# 
# 
# 
# Example 2:
# 
# 
# Input: R = 2, C = 2, r0 = 0, c0 = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
# 
# 
# 
# Example 3:
# 
# 
# Input: R = 2, C = 3, r0 = 1, c0 = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as
# [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
# 
# 
# 
# 
# 
#
class Solution:
    # def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    def allCellsDistOrder(self, R, C, r0, c0):
        m = [[x, y] for x in range(R) for y in range(C)]
        d = [abs(x[0] - r0) + abs(x[1] - c0) for x in m]
        # print(m)
        # print(d)
        # m = sorted(m, key=d)

        return [x for _ , x in sorted(zip(d,m))]






    """
    def allCellsDistOrder(self, R, C, r0, c0):
        self.l = []
        self.q = [(r0, c0)]
        def recur(x, y):
            if [x, y] not in self.l:
                self.l.append([x, y])
            
                self.q.append((x, y))
            else:
                if x > 0 and [x-1, y] not in self.l:
                    self.l.append([x-1, y])
                    self.q.append((x-1, y))
                if x < R - 1 and [x+1, y] not in self.l:
                    self.l.append([x+1, y])
                    self.q.append((x+1, y))
                # left
                if y > 0 and [x, y-1] not in self.l:
                    self.l.append([x, y-1])
                    self.q.append((x, y-1))
                # right
                if y < C - 1 and [x, y+1] not in self.l:
                    self.l.append([x, y+1])
                    self.q.append((x, y+1))
                
        while self.q:
            # print(self.q)
            recur(*self.q.pop(0))
        return self.l
    """
# s = Solution()
# print(s.allCellsDistOrder(1, 2, 0, 0))


# # s = Solution()
# print(s.allCellsDistOrder(2, 2, 0, 1))



# print(s.allCellsDistOrder(2, 3, 1, 2))
# print(s.allCellsDistOrder(89, 90, 21, 65))































