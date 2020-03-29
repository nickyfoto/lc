#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (54.60%)
# Total Accepted:    28.3K
# Total Submissions: 51.7K
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
class UF:
    def __init__(self, n):
        self.arr = list(range(n))
        self.count = n
    
    def find(self, p):
        while p != self.arr[p]:
            p = self.arr[p]
        return p

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return
        self.arr[rootA] = rootB
        self.count -= 1

class Solution:
    # def removeStones(self, stones: List[List[int]]) -> int:
    def removeStones(self, stones):
        # stones.sort()
        

        total = len(stones)
        uf = UF(total)

        
        
        for i in range(total):
            for j in range(i+1, total):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        
        # print(uf.count)

        return total - uf.count



# s = Solution()
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# print(s.removeStones(stones))

# stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# print(s.removeStones(stones))

# stones = [[0,0]]
# print(s.removeStones(stones))







