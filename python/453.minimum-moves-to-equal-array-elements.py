#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (49.07%)
# Total Accepted:    57K
# Total Submissions: 116K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array of size n, find the minimum number of moves
# required to make all array elements equal, where a move is incrementing n - 1
# elements by 1.
# 
# Example:
# 
# Input:
# [1,2,3]
# 
# Output:
# 3
# 
# Explanation:
# Only three moves are needed (remember each move increments two elements):
# 
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# 
#
class Solution:
    # def minMoves(self, nums: List[int]) -> int:
    def minMoves(self, nums):



        def func1(nums):
            n = len(nums)
            if n == 1:
                return 0
            nums.sort()
            first = nums[0]
            while nums[0] != nums[-1]:
                for i in range(n-1):
                    larger_idx = 0
                    if nums[i] == nums[-1]:
                        larger_idx = i
                    nums[i] += max(1, nums[-1] - nums[-2])
                    if larger_idx:
                        nums[-1], nums[larger_idx] = nums[larger_idx], nums[-1]      
            return nums[-1]-first


        def func2(nums):
            n = len(nums)
            if n == 1:
                return 0
            nums.sort()
            diff = nums[-1] - nums[0]
            s = (1 + diff) * diff // 2
            element = nums[0]
            idx = 0
            while element <= nums[-1]:
                count = 0
                # print("start element=", element)
                while idx < n and nums[idx] == element:
                    count += 1
                    idx += 1
                if count == 0:
                    # print("when count == 0")
                    # print(nums[idx-1], nums[idx], element - nums[0])
                    # print(list(range(element, nums[idx])))
                    # print(element + len(list(range(element, nums[idx]))))
                    length = (nums[idx]-element)
                    total_miss = (element + nums[idx]-1)* length // 2 - length * nums[0]
                    s -= total_miss
                    # s -= element - nums[0]
                    element += length-1
                elif count > 1:
                    s += (element - nums[0]) * (count-1)
                # if idx < n:
                    # print(nums[idx])
                # print("finish element=", element)
                element += 1
            return s
        
        # nums.sort()
        # n = len(nums)

        # diff = nums[-1] - nums[0]
        # if diff < n*10:
        #     return func1(nums)
        # else:
        return func2(nums)



