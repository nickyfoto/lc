#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (49.98%)
# Total Accepted:    241.8K
# Total Submissions: 481.3K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
# 
# Note:
# 
# 
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Example:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
#
class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def bs(self, numbers, target, debug=False):
        if debug:
            print("numbers=", numbers, "target=", target)
        if target > numbers[-1] or target < numbers[0]:
            return False
        n = len(numbers)
        if n == 1:
            if numbers[0] == target:
                return 1
            else:
                return False
        mid = n // 2
        if numbers[mid] == target:
            return mid + 1
        elif target < numbers[mid]:
            res = self.bs(numbers[:mid], target)
            if res:
                return res
            else:
                return False
        else:
            res = self.bs(numbers[mid:], target)
            if res:
                return mid + res
            else:
                return False

    def twoSum(self, numbers, target, debug=False):
        if target < numbers[0]:
            return False
        n = len(numbers)
        if n == 2:
            if sum(numbers) == target:
                return [1, 2]
        mid = n // 2
        if numbers[mid] > target:
            return self.twoSum(numbers[:mid], target)
        elif numbers[mid] == target:
            return [self.twoSum(numbers[:mid], 0), mid]
        else:
            if debug:
                print(numbers, target, n)
            for i in range(n):
                diff = target - numbers[i]
                if diff >= numbers[i]:
                    if debug:
                        print("i=", i, 'diff=', diff)
                    diff_idx = self.bs(numbers[i:], diff)
                    if debug:
                        print('diff_idx=', diff_idx)
                    if diff_idx:
                        return [i+1, i+diff_idx]


    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        res = []
        while l <= r:
            sm = numbers[l] + numbers[r]
            if sm == target:
                res = [l + 1, r + 1]
                break
            elif target < sm:
                r -= 1
            else:
                l += 1
        return res
# s = Solution()
# a = [2,7,11,15]
# target = 9
# print(s.twoSum(a, target))
# a = [0,1,2,7,11,15]
# target = 9
# print(s.twoSum(a, target))
# a = [0,1,2,7,11,15]
# target = 16
# print(s.twoSum(a, target))

# a = [0,1,2,7,11,15]
# target = 15
# print(s.twoSum(a, target))

# a = [0,1,2,7,11,15]
# target = 26
# print(s.twoSum(a, target))



# a = [1,2,3,4,4,9,56,90]
# target = 8
# print(s.twoSum(a, target))






