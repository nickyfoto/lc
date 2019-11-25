#
# @lc app=leetcode id=452 lang=python3

# Input:
# [[10,16], [2,8], [1,6], [7,12]]
# 
# Output:
# 2
# 
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons
# [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two
# balloons).
# 
# 
# 
# 
#
class Solution:
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    def findMinArrowShots(self, points):
        points.sort()
        # print(points)
        n = len(points)
        i = 0
        shot = 0
        while i < n:
            right = points[i][1]
            j = i + 1
            while j < n and points[j][0] <= right:
                right = min(right, points[j][1])
                j += 1
            i = j
            shot += 1
        return shot


# s = Solution()
# points = [[10,16], [2,8], [1,6], [7,12]]
# print(s.findMinArrowShots(points) == 2)

# points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
# print(s.findMinArrowShots(points) == 2) # 2