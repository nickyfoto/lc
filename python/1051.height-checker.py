#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#
# https://leetcode.com/problems/height-checker/description/
#
# algorithms
# Easy (69.84%)
# Total Accepted:    11.3K
# Total Submissions: 16.3K
# Testcase Example:  '[1,1,4,2,1,3]'
#
# Students are asked to stand in non-decreasing order of heights for an annual
# photo.
# 
# Return the minimum number of students not standing in the right positions.
# (This is the number of students that must move in order for all students to
# be standing in non-decreasing order of height.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# Students with heights 4, 3 and the last 1 are not standing in the right
# positions.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100
# 
#
class Solution:
    # def heightChecker(self, heights: List[int]) -> int:
    def heightChecker(self, heights):
        n = len(heights)
        heights = [(heights[idx], idx) for idx in range(n)]
        # moves = 0
        i = 0
        moves = []
        while i < n:
            Min = heights[i][0]
            Min_idx = i
            j = i + 1
            while j < n:
            # for j in range(i+1, n):
                # print('i=', i, 'j=', j)
                if heights[j][0] <= Min:
                    Min = heights[j][0]
                    Min_idx = j
                j += 1
            if Min < heights[i][0] and Min_idx != i:
                heights[i], heights[Min_idx] = heights[Min_idx], heights[i]
                if heights[i][1] not in moves:
                    moves.append(heights[i][1])
                if heights[Min_idx][1] not in moves:
                    moves.append(heights[Min_idx][1])
                # print(moves)
                # moves += 1
                # print('i=', i, heights)
                # i = j+1
            # else:
                # print('i=', i)
            i += 1
        return len(moves)


# s = Solution()
# heights = [1,1,4,2,1,3]
# print(s.heightChecker(heights) == 3)




# heights = [2,1,2,1,1,2,2,1]
# print(s.heightChecker(heights) == 4)