#
# @lc app=leetcode id=519 lang=python3
#
# [519] Random Flip Matrix
#
# https://leetcode.com/problems/random-flip-matrix/description/
#
# algorithms
# Medium (33.68%)
# Total Accepted:    4.9K
# Total Submissions: 14.4K
# Testcase Example:  '["Solution", "flip", "flip", "flip", "flip"]\n[[2, 2], [], [], [], []]'
#
# You are given the number of rows n_rows and number of columns n_cols of a 2D
# binary matrix where all values are initially 0. Write a function flip which
# chooses a 0 value uniformly at random, changes it to 1, and then returns the
# position [row.id, col.id] of that value. Also, write a function reset which
# sets all values back to 0. Try to minimize the number of calls to system's
# Math.random() and optimize the time and space complexity.
# 
# Note:
# 
# 
# 1 <= n_rows, n_cols <= 10000
# 0 <= row.id < n_rows and 0 <= col.id < n_cols
# flip will not be called when the matrix has no 0 values left.
# the total number of calls to flip and reset will not exceed 1000.
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# Output: [null,[0,1],[1,2],[1,0],[1,1]]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# Output: [null,[0,0],[0,1],null,[0,0]]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, n_rows and n_cols. flip and reset
# have no arguments. Arguments are always wrapped with a list, even if there
# aren't any.
# 
#
from random import choices, randint
# from collections import defaultdict
class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.end = n_rows*n_cols - 1
        self.start = 0
        self.d = {}
        # self.pool = range(self.n)
        # self.weights = [1] * self.n

    # def flip(self) -> List[int]:
    def flip(self):
        # print(self.n_rows, self.n_cols)
        rand = randint(self.start, self.end)
        res = self.d.get(rand, rand)
        self.d[rand] = self.d.get(self.start, self.start)
        self.start += 1
        return divmod(res, self.n_cols)

        # idx = choices(self.pool, weights=self.weights)[0]
        # quo, r = divmod(idx, self.n_cols)
        # self.weights[idx] = 0
        # return [quo, r]
        

    def reset(self) -> None:
        # self.weights = [1] * self.n
        self.d = {}
        self.start = 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(2, 3)
# print(obj.flip())
# print(obj.flip())
# print(obj.flip())
# print(obj.flip())
# print(obj.flip())
# print(obj.flip())

# obj = Solution(1, 2)
# print(obj.flip())
# print(obj.flip())
# obj.reset()
# print(obj.flip())
# print(obj.flip())



# print(choices(range(2), weights=[0,1]))














