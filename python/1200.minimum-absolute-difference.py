#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#
# https://leetcode.com/problems/minimum-absolute-difference/description/
#
# algorithms
# Easy (67.41%)
# Total Accepted:    7.1K
# Total Submissions: 10.5K
# Testcase Example:  '[4,2,1,3]'
#
# Given an array of distinct integers arr, find all pairs of elements with the
# minimum absolute difference of any two elements. 
# 
# Return a list of pairs in ascending order(with respect to pairs), each pair
# [a, b] follows
# 
# 
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in
# arr
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with
# difference equal to 1 in ascending order.
# 
# Example 2:
# 
# 
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# 
# 
# Example 3:
# 
# 
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6
# 
# 
#
class Solution:
    # def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    def minimumAbsDifference(self, arr):

        arr.sort()
        n = len(arr)
        d = {}
        mn = float('inf')
        for i in range(1,n):
            diff = arr[i] - arr[i-1]
            if diff <= mn:
                mn = diff
                d[(arr[i-1], arr[i])] = diff


        # arr.sort(reverse=True)
        # for i in range(1,n):
            # d[(arr[i], arr[i-1])] = arr[i-1] - arr[i]
            # mn = min(mn, arr[i-1] - arr[i])



        # print(d)
        return [list(k) for k,v in d.items() if v == min(d.values())]


# s = Solution()
# arr = [4,2,1,3]
# print(s.minimumAbsDifference(arr))

# arr = [3,8,-10,23,19,-4,-14,27]
# print(s.minimumAbsDifference(arr))


# arr = [1,3,6,10,15]
# print(s.minimumAbsDifference(arr))








        
