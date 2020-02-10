#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#
# https://leetcode.com/problems/prison-cells-after-n-days/description/
#
# algorithms
# Medium (39.12%)
# Likes:    310
# Dislikes: 533
# Total Accepted:    36.3K
# Total Submissions: 92.8K
# Testcase Example:  '[0,1,0,1,1,0,0,1]\n7'
#
# There are 8 prison cells in a row, and each cell is either occupied or
# vacant.
# 
# Each day, whether the cell is occupied or vacant changes according to the
# following rules:
# 
# 
# If a cell has two adjacent neighbors that are both occupied or both vacant,
# then the cell becomes occupied.
# Otherwise, it becomes vacant.
# 
# 
# (Note that because the prison is a row, the first and the last cells in the
# row can't have two adjacent neighbors.)
# 
# We describe the current state of the prison in the following way: cells[i] ==
# 1 if the i-th cell is occupied, else cells[i] == 0.
# 
# Given the initial state of the prison, return the state of the prison after N
# days (and N such changes described above.)
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
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: 
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]
# 
# 
# 
# 
# Note:
# 
# 
# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    # def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    def prisonAfterNDays(self, cells, N):
        if N % 14 == 0 and cells[0] == 0 and cells[7] == 0:
            return cells
        # day one
        i = 0
        def change(snap, cells):
            for i in range(8):
                if i == 0 or i == 7:
                    if snap[i] == 1:
                        cells[i] = 0
                else:
                    if snap[i - 1] == snap[i + 1]:
                        cells[i] = 1
                    else:
                        cells[i] = 0
            return cells
        
        while i < N:
            snap = cells.copy()
            if i == 1:
                day_one = snap
            cells = change(snap, cells)
            if i > 1 and cells == day_one:
                # print('i=', i, N % i, day_one, snap)
                if N % 14 == 0:
                    return snap
                else:
                    return self.prisonAfterNDays(cells, N % 14 - 1)
                # todo
            i += 1
        return cells
        
        
        
        
# @lc code=end
