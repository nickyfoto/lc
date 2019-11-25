#
# @lc app=leetcode id=754 lang=python3
#
# [754] Reach a Number
#
# https://leetcode.com/problems/reach-a-number/description/
#
# algorithms
# Easy (32.12%)
# Total Accepted:    10.2K
# Total Submissions: 31.3K
# Testcase Example:  '1'
#
# 
# You are standing at position 0 on an infinite number line.  There is a goal
# at position target.
# 
# On each move, you can either go left or right.  During the n-th move
# (starting from 1), you take n steps.
# 
# Return the minimum number of steps required to reach the destination.
# 
# 
# Example 1:
# 
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
# 
# 
# 
# Example 2:
# 
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
# 
# 
# 
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].
# 
#
class Solution:
    # def reachNumber(self, target: int) -> int:
    def reachNumber(self, target, debug=False):
        if target < 0:
            target = - target
        total = 0
        i = 0
        while True:
            total += i
            if target % 2 == 0 and total % 2 == 0:
                if target <= total:
                    return i
            elif target % 2 == 1 and total % 2 == 1:
                if target <= total:
                    return i
            i += 1
            # print(i, total)





















    # def reachNumber(self, target, debug=False):
    #     # pos left, pos_right
        
        # count = 0
        # reaches = [0]
        # while target not in reaches:
        #     count += 1
        #     new_reaches = []
        #     for r in reaches:
        #         new_reaches.append(r+count)
        #         new_reaches.append(r-count)
        #     reaches = new_reaches
        #     print(sorted(reaches)) if debug else None
        # return count

    # def reachNumber(self, target, debug=False):
        
        
    #     count = 0
    #     q = [(0, 1)]
    #     def bfs(point):
    #         pos, step = point
    #         print('pos=', pos, 'step=', step) if debug else None
    #         l, r = pos - step, pos + step

    #         # print('l=', l, 'r=', r)
    #         if l == target or r == target:
    #             return step
    #         else:
    #             # print('here')
    #             q.append((l, step + 1))
    #             q.append((r, step + 1))
    #             # print(q)
    #         while q:
    #             return bfs(q.pop(0))    
            
    #     return bfs(q.pop(0))






























