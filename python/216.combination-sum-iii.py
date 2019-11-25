#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (53.17%)
# Total Accepted:    136.1K
# Total Submissions: 256K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#
class Solution:
    # def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    def combinationSum3(self, k: int, n: int):

        if k == 1:
            return [[n]]
        if n // k >= 9:
            return []
        if k > n:
            return []


        def recur(k, n, start):
            # print('k=', k, 'n=', n, 'start=', start)
            if start > n:
                return []

            if k == 1:
                if n > 9:
                    return []
                return [[n]]

            l = []
            start = max(start, n - 9 * (k-1))

            test_start = start + 1


            test_end = test_start + k - 1

            while (test_start+test_end) * k // 2 <= n:
                test_start += 1
                test_end += 1
            # print('test_start =', test_start)
            
            end = test_start
            # print('end=', end)
            for i in range(start, end):
                res = recur(k-1, n-i, i+1)
                for r in res:
                    l.append([i] + r)
            return l

        # print(recur(k, n, start=1))
        return recur(k, n, start=1)



# s = Solution()

# k = 3
# n = 7
# print(s.combinationSum3(k, n))


# k = 3
# n = 9
# print(s.combinationSum3(k, n))


# k = 2
# n = 18
# print(s.combinationSum3(k, n))


# k = 3
# n = 15
# print(s.combinationSum3(k, n))


# k = 3
# n = 2
# print(s.combinationSum3(k, n))



# k = 4
# n = 24
# print(s.combinationSum3(k, n))





        
