#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (24.11%)
# Total Accepted:    164.2K
# Total Submissions: 681.2K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#

class UF:
    
    def __init__(self, total):
        self.arr = list(range(total))
        # self.count = total

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
        # self.count -= 1


from collections import defaultdict

class Solution:
    # def solve(self, board: List[List[str]]) -> None:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        explored = defaultdict(lambda: False)

        def reach_border(r, c):
            return r == 0 or r == n_rows - 1 or c == 0 or c == n_cols - 1

        class Node:
            def __init__(self, point, border):
                # print('point=', point)
                self.r, self.c = point
                self.points = {point: 1}
                self.border = border

            def valid(self, r, c):
                return r >= 0 and r < n_rows and c >= 0 and c < n_cols

            

            def explore(self, r, c):
                # print(r,c)
                if self.valid(r,c) and not explored[(r,c)] and board[r][c] == 'O':
                    if not self.border:
                        if reach_border(r, c):
                            self.border = True
                    explored[(r,c)] = True
                    # node = Node((r, c), border=self.border)
                    # node.dfs()
                    # if not self.border:
                        # self.border = node.border
                    return {(r,c): 1}
                else:
                    return {}
                

            def up(self, r, c):
                r, c = r - 1, c
                return self.explore(r, c)

            def down(self, r, c):
                r, c = r + 1, c
                return self.explore(r, c)

            def left(self, r, c):
                r, c = r, c - 1
                return self.explore(r, c)

            def right(self, r, c):
                r, c = r, c + 1        
                return self.explore(r, c)


            def bfs(self):
                self.round = {(self.r, self.c): 0}
                while self.round:
                    temp = {}
                    for point in self.round:
                        r, c = point
                        temp.update(self.up(r,c))
                        temp.update(self.down(r,c))
                        temp.update(self.left(r,c))
                        temp.update(self.right(r,c))
                    if temp:
                        self.points.update(temp)
                    self.round = temp
                    # else:
                        # self.round = 



        nodes = []
        n_rows = len(board)
        n_cols = len(board[0])


        # print(n_rows, n_cols)

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == 'O':
                    point = r, c
                    if not explored[point]:
                        node = Node(point, border=reach_border(r,c))
                        explored[point] = True
                        node.bfs()
                        nodes.append(node)

        # print(nodes)

        for node in nodes:
            # print(node.border, node.points)
            if not node.border:
                for r,c in node.points:
                    board[r][c] = 'X'
        # print(board)



# s = Solution()
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# print(s.solve(board))


















        
