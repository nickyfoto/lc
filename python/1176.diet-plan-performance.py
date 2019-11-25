#
# @lc app=leetcode id=1176 lang=python3
#
# [1176] Diet Plan Performance
#
# https://leetcode.com/problems/diet-plan-performance/description/
#
# algorithms
# Easy (43.72%)
# Total Accepted:    3.3K
# Total Submissions: 7.7K
# Testcase Example:  '[1,2,3,4,5]\n1\n3\n3'
#
# A dieter consumes calories[i] calories on the i-th day.  For every
# consecutive sequence of k days, they look at T, the total calories consumed
# during that sequence of k days:
# 
# 
# If T < lower, they performed poorly on their diet and lose 1 point; 
# If T > upper, they performed well on their diet and gain 1 point;
# Otherwise, they performed normally and there is no change in points.
# 
# 
# Return the total number of points the dieter has after all calories.length
# days.
# 
# Note that: The total points could be negative.
# 
# 
# Example 1:
# 
# 
# Input: calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3
# Output: 0
# Explaination: calories[0], calories[1] < lower and calories[3], calories[4] >
# upper, total points = 0.
# 
# Example 2:
# 
# 
# Input: calories = [3,2], k = 2, lower = 0, upper = 1
# Output: 1
# Explaination: calories[0] + calories[1] > upper, total points = 1.
# 
# 
# Example 3:
# 
# 
# Input: calories = [6,5,0,0], k = 2, lower = 1, upper = 5
# Output: 0
# Explaination: calories[0] + calories[1] > upper, calories[2] + calories[3] <
# lower, total points = 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= calories.length <= 10^5
# 0 <= calories[i] <= 20000
# 0 <= lower <= upper
# 
# 
#
class Solution:
    # def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        n = len(calories)
        score = 0
        total = sum(calories[:k])
        for i in range(0, n-k+1):
            # print(i)
            
            # print(calories[i:i+k], total)
            if total < lower:
                score -= 1
            elif total > upper:
                score += 1
            if i+k < n:
                total -= calories[i]
                total += calories[i+k]
        return score

# s = Solution()
# calories = [6,5,0,0]
# k = 2
# lower = 1
# upper = 5
# print(s.dietPlanPerformance(calories, k, lower, upper))

# calories = [3,2]
# k = 2
# lower = 0
# upper = 1
# print(s.dietPlanPerformance(calories, k, lower, upper))


# calories = [6,13,8,7,10,1,12,11]
# k = 6
# lower = 5
# upper = 37
# print(s.dietPlanPerformance(calories, k, lower, upper))