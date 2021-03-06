#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#
# https://leetcode.com/problems/friend-circles/description/
#
# algorithms
# Medium (54.69%)
# Total Accepted:    99.9K
# Total Submissions: 182.6K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 
# There are N students in a class. Some of them are friends, while some are
# not. Their friendship is transitive in nature. For example, if A is a direct
# friend of B, and B is a direct friend of C, then A is an indirect friend of
# C. And we defined a friend circle is a group of students who are direct or
# indirect friends.
# 
# 
# 
# Given a N*N matrix M representing the friend relationship between students in
# the class. If M[i][j] = 1, then the ith and jth students are direct friends
# with each other, otherwise not. And you have to output the total number of
# friend circles among all the students.
# 
# 
# Example 1:
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a
# friend circle. The 2nd student himself is in a friend circle. So return 2.
# 
# 
# 
# Example 2:
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
# students are direct friends, so the 0th and 2nd students are indirect
# friends. All of them are in the same friend circle, so return 1.
# 
# 
# 
# 
# Note:
# 
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.
# 
# 
#


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
    # def findCircleNum(self, M: List[List[int]]) -> int:
    def findCircleNum(self, M) -> int:
        

        total = len(M)
        uf = UF(total)
        for r in range(total):
            for c in range(r+1, total):
                # print(r, c)
                if M[r][c]:
                    uf.union(r,c)
        # print(uf.count)
        return uf.count


# s = Solution()
# M = [[1,1,0],[1,1,0],[0,0,1]]
# print(s.findCircleNum(M))

# M = [[1,1,0],[1,1,1],[0,1,1]]
# print(s.findCircleNum(M))


















