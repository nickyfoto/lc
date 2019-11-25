#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#
# https://leetcode.com/problems/spiral-matrix-iii/description/
#
# algorithms
# Medium (65.53%)
# Total Accepted:    11.1K
# Total Submissions: 16.9K
# Testcase Example:  '1\n4\n0\n0'
#
# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0)
# facing east.
# 
# Here, the north-west corner of the grid is at the first row and column, and
# the south-east corner of the grid is at the last row and column.
# 
# Now, we walk in a clockwise spiral shape to visit every position in this
# grid. 
# 
# Whenever we would move outside the boundary of the grid, we continue our walk
# outside the grid (but may return to the grid boundary later.) 
# 
# Eventually, we reach all R * C spaces of the grid.
# 
# Return a list of coordinates representing the positions of the grid in the
# order they were visited.
# 
# 
# 
# Example 1:
# 
# 
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
# 
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output:
# [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
# 
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
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
# 
# 
# 
# 
#
class Solution:
    # def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        

        number_of_corners = set([(0,0), (0, C-1), (R-1, 0), (R-1,C-1)])
        
        # print(number_of_corners)
        
        d = {}
        self.n = 0
        
        def valid(point):
            if point in number_of_corners:
                self.n += 1
            return self.n

        def valid_left(p, left):
            if p[0] < 0:
                return self.n
            if left[1] < C:
                end = left[1]+1
            else:
                end = C
            for i in range(p[1]+1, end):

                point = (p[0], i)
                if point[1] < C and point[1] >= 0:
                # print(point)
                    d[point] = 1
                    self.n = valid(point)
            return self.n
        
        def valid_up(p, up):
            # print(p, up)
            if p[1] < 0:
                return self.n
            if up[0] < 0:
                end = -1
            else:
                end = up[0] - 1
            for i in range(p[0]-1, end, - 1):
                point = (i, p[1])
                
                if point[0] >= 0 and point[0] < R:
                    d[point] = 1
                    self.n = valid(point)
            return self.n


        def valid_down(p, down):
            # print('here', p, down)
            if p[1] >= C:
                return self.n
            if down[0] < R:
                end = down[0] + 1
            else:
                end = R
            for i in range(p[0]+1, end):
                point = (i, p[1])
                if point[0] >= 0 and point[0] < R:
                    d[point] = 1
                    self.n = valid(point)
            return self.n

        def valid_right(p, right):
            # print('p=', p)
            # print('right=', right)
            if p[0] >= R:
                # print('here')
                return self.n
            if right[1] < 0:
                end = - 1
            else:
                end = right[1] - 1
            for i in range(p[1]-1, end, -1):
                point = (p[0],i)
                # print('       checking', point)
                if point[1] >= 0 and point[1] < C:
                    d[point] = 1
                    self.n = valid(point)
            return self.n




        step = 1
        p = (r0, c0)
        self.n = valid((r0,c0))
        d[p] = 1
        while self.n < len(number_of_corners):

            left = (p[0], p[1]+step)
            self.n = valid_left(p, left)
            p = left
            # print('left=', left)


            down = (p[0]+step, p[1])
            self.n = valid_down(p, down)
            step += 1
            p = down
            # print('down', down)


            # print('d=', d)
            right = (p[0], p[1]-step)
            self.n = valid_right(p, right)
            p = right
            # print('right', right)

            # print('step', step)
            up = (p[0]-step, p[1])
            self.n = valid_up(p, up)
            p = up
            # print('up=', up)


            step += 1




        # print(self.n)
        # print(d)
        return [list(k) for k in d]



s = Solution()
# R = 1
# C = 4
# r0 = 0
# c0 = 0
# # print(s.spiralMatrixIII(R, C, r0, c0))




# R = 5
# C = 6
# r0 = 1
# c0 = 4
# print(s.spiralMatrixIII(R, C, r0, c0) == [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])



# [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]
# # below is correct
# [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4], [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2], [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]



# R = 3
# C = 3
# r0 = 2
# c0 = 0
# print(s.spiralMatrixIII(R, C, r0, c0) == [[2,0],[2,1],[1,0],[1,1],[1,2],[2,2],[0,0],[0,1],[0,2]])
# # correct 
# [[2,0],[2,1],[1,0],[1,1],[1,2],[2,2],[0,0],[0,1],[0,2]]


# R = 3
# C = 3
# r0 = 2
# c0 = 2
# print(s.spiralMatrixIII(R, C, r0, c0) == [[2,2],[2,1],[1,1],[1,2],[2,0],[1,0],[0,0],[0,1],[0,2]])
# # correct
# [[2,2],[2,1],[1,1],[1,2],[2,0],[1,0],[0,0],[0,1],[0,2]]
