#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (44.91%)
# Total Accepted:    13.5K
# Total Submissions: 29.9K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
# 
# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.
# 
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,1],[1,0]]
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1
# 
# 
# 
# 
# 
# 
# 
#

from collections import defaultdict











class Solution:
    # def shortestBridge(self, A: List[List[int]]) -> int:
    def shortestBridge(self, A) -> int:
        # islands = []
        n_rows = len(A)
        n_cols = len(A[0])


        class Island:
            def __init__(self, point):
                # print(point)
                self.r, self.c = point
                self.points = {point: 1}
                self.dfs()

            def valid(self, r, c):
                return r >= 0 and r < n_rows and c >= 0 and c < n_cols

            def explore(self, r, c):
                if self.valid(r,c) and not explored[(r,c)] and A[r][c]:
                    explored[(r,c)] = True
                    island = Island((r, c))
                    island.dfs()
                    return island.points
                else:
                    return {}
            def up(self):
                r, c = self.r - 1, self.c
                return self.explore(r, c)

            def down(self):
                r, c = self.r + 1, self.c
                return self.explore(r, c)

            def left(self):
                r, c = self.r, self.c - 1
                return self.explore(r, c)

            def right(self):
                r, c = self.r, self.c + 1        
                return self.explore(r, c)

            def dfs(self):
                self.points.update(self.up())
                self.points.update(self.down())
                self.points.update(self.left())
                self.points.update(self.right())

            def _discover(self, r, c):
                # print((r,c), self.valid(r, c), not explored[(r,c)])
                if self.valid(r, c) and not explored[(r,c)]:
                    if not A[r][c]:
                        # print('here')
                        self.expansion[(r,c)] = 1
                        explored[(r,c)] = True
                        return False
                    else:
                        return True
                else:
                    return False
            def discover(self, point):
                old_r, old_c = point
                r, c = old_r - 1, old_c
                up = self._discover(r, c)
                r, c = old_r + 1, old_c
                down = self._discover(r, c)
                r, c = old_r, old_c - 1
                left = self._discover(r, c)
                r, c = old_r, old_c + 1
                right = self._discover(r, c)
                # print(up, down ,left, right)
                return up or down or left or right




            def bfs(self):
                # print(self.points)
                # print(len(self.points))
                # print(len([(k,v) for k,v in explored.items() if v]))
                self.territory = self.points
                self.expansion = {}
                self.steps = 0
                found = False
                while not found:
                    for point in self.territory:
                        found = self.discover(point)
                        # print(found)
                        if found:
                            break
                    self.steps += 1
                    # print('here', self.expansion)
                    self.territory = self.expansion
                    self.expansion = {}
                # print(steps)


        explored = defaultdict(lambda: False)
        island = None
        for i in range(n_rows):
            for j in range(n_cols):
                if A[i][j]:
                    island = Island((i,j))
                    explored[(i,j)] = True
                    break
            if island:
                break
        # print(island.points)
        island.bfs()
        # print(island.steps)        
        return island.steps - 1



# s = Solution()
# A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# print(s.shortestBridge(A))




# A = [[0,1],[1,0]]
# print(s.shortestBridge(A))


# A = [[0,1,0],[0,0,0],[0,0,1]]
# print(s.shortestBridge(A))




# A = [[0,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
# print(s.shortestBridge(A)) # 1
















        
