#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (29.03%)
# Total Accepted:    97.4K
# Total Submissions: 333.4K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
class Solution:
    # def thirdMax(self, nums: List[int]) -> int:
    def thirdMax(self, nums):
        n = len(nums)
        if n < 3:
            return max(nums)
        top3 = []
        for i in nums:

            if not top3:
                top3.append(i)
            elif len(top3) == 1:
                if top3[0] < i:
                    top3.append(i)
                elif i < top3[0]:
                    top3.insert(0, i)
            elif len(top3) == 2:
                # [1,2]
                if top3[-1] < i:
                    top3.append(i)
                elif i < top3[0]:
                    top3.insert(0, i)
                elif top3[0] < i and i < top3[-1]:
                    top3.insert(1, i)
            else:
                # len(top3) == 3
                # [1,2,3]
                
                if top3[0] < i and i < top3[1]:
                    top3[0] = i
                    # if i == 9989:
                        # print(i, top3, top3[0] < i, i < top3[1])
                elif top3[1] < i and i < top3[2]:
                    top3.pop(0)
                    top3.insert(1, i)
                elif top3[2] < i:
                    top3.pop(0)
                    top3.append(i)
        if len(top3) < 3:
            return max(nums)
        # print(top3)
        return top3[0]

# s = Solution()
# nums = [3, 2, 1]
# print(s.thirdMax(nums))


# nums = [2, 2, 3, 1]
# print(s.thirdMax(nums))














