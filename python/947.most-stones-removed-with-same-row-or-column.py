#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (54.95%)
# Likes:    744
# Dislikes: 241
# Total Accepted:    40.6K
# Total Submissions: 73.9K
# Testcase Example:  '[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]'
#
# On a 2D plane, we place stones at some integer coordinate points.  Each
# coordinate point may have at most one stone.
# 
# Now, a move consists of removing a stone that shares a column or row with
# another stone on the grid.
# 
# What is the largest possible number of moves we can make?
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# 
# 
# 
# Example 2:
# 
# 
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: stones = [[0,0]]
# Output: 0
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    # def removeStones(self, stones: List[List[int]]) -> int:
    def removeStones(self, stones):
        class UF:
            def __init__(self, total):
                self.arr = range(total)
            def find(self, p):
                while p != self.arr[p]:
                    p = self.arr[p]
                return p
            def union(self, p, q):
                root_p = self.find(p)
                root_q = self.find(q)
                self.arr[root_q] = root_p
        uf = UF(20000)
        for x, y in stones:
            uf.union(x, y + 100000)
        return len(stones) - {uf.find(x) for x, y in stones}
# @lc code=end
