#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (20.10%)
# Total Accepted:    100.6K
# Total Submissions: 500.3K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
#
import bisect
class Solution:
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    def containsNearbyAlmostDuplicate2(self, nums, k: int, t: int) -> bool:
        K = k
        if len(nums) < 2:
            return False
        if K == 0:
            return False
        n = len(nums)

        def check(arr,k):
            arr.sort()
            i = 1
            while i < k+1:
                if arr[i] - arr[i-1] <= t:
                    return True
                i += 1
            return False

        for k in range(1, K+1):
            print('k=', k)
            for i in range(0,n-k):
                # print('k=',k,'i=', i, 'i+k+1=',i+k+1)
                arr = nums[i:i+k+1]
                print(arr)
                if check(arr, k):
                    return True
        return False
            # else:
                # arr = nums[i-k:i+k+1]
                # print(arr)




    def containsNearbyAlmostDuplicate1(self, nums, k: int, t: int) -> bool:

        def check(arr,k):
            arr.sort()
            i = 1
            while i < k+1:
                if arr[i] - arr[i-1] <= t:
                    return True
                i += 1
            return False

        n = len(nums)
        # print(n)
        if n - k <= 0:
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= t:
                    return True
                i += 1
            return False

        for i in range(0,n-k):
            # print('k=',k,'i=', i, 'i+k+1=',i+k+1)
            # print('i=', i)
            arr = nums[i:i+k+1]
            print(arr)
            if check(arr, k):
                return True
        return False



    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if len(nums) < 2:
            return False
        if k == 0:
            return False
        def check(arr,k):
            arr.sort()
            i = 1
            while i < k+1:
                if arr[i] - arr[i-1] <= t:
                    # print('here')
                    return True, arr
                i += 1
            return False, arr

        # print(arr)
        d = {}
        for i, v in enumerate(nums):
            d[i] = v
        # print(d)
        n = len(nums)

        if n - k <= 0:
            i = 1
            nums.sort()
            while i < n:
                if nums[i] - nums[i-1] <= t:
                    return True
                i += 1
            return False

        arr = nums[:k+1]
        ans, sorted_arr = check(arr, k)
        if ans:
            return True
        else:
            # print(sorted_arr)
            for i in range(k+1, n):
                # print(nums[i])
                # print('i=',i, sorted_arr)
                # print('i-(k+1)=', i-(k+1), d)
                sorted_arr.remove(d[i-(k+1)])
                # print(sorted_arr, nums[i])
                idx = bisect.bisect_left(sorted_arr, nums[i])
                # print(sorted_arr, idx, 'k-1=', k-1)
                if idx == 0: #insert position == 0
                    if sorted_arr[0] - nums[i] <= t:
                        return True
                elif idx == k: #insert outside sorted_arr
                    if nums[i] - sorted_arr[-1] <= t:
                        return True
                else:
                    # print('here', nums[i], sorted_arr,idx)
                    if sorted_arr[idx] - nums[i] <= t or nums[i] - sorted_arr[idx-1] <= t:
                        return True
                sorted_arr.insert(idx, nums[i])
            return False




s = Solution()
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(s.containsNearbyAlmostDuplicate(nums, k, t) == False)


nums = [1,0,1,1]
k = 1
t = 2
print(s.containsNearbyAlmostDuplicate(nums, k, t))



nums = [1,2,3,1]
k = 3
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k, t))



nums = [0]
k = 0
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k, t) == False)


nums = [-3,3]
k = 2
t = 4
print(s.containsNearbyAlmostDuplicate(nums, k, t) == False) #False

nums = [2,2]
k = 3
t = 0
print(s.containsNearbyAlmostDuplicate(nums, k, t)) #True

nums = [10,100,11,9,100,10]
k = 1
t = 2
print(s.containsNearbyAlmostDuplicate(nums, k, t)) #True


nums = [1,2]
k = 0
t = 1
print(s.containsNearbyAlmostDuplicate(nums, k, t) == False) #False

nums = [4,2]
k = 2
t = 1
print(s.containsNearbyAlmostDuplicate(nums, k, t) == False) #False



nums = [3,6,0,4]
k = 2
t = 2
print(s.containsNearbyAlmostDuplicate(nums, k, t)) #True


nums = [3,6,0,2]
k = 2
t = 2
print(s.containsNearbyAlmostDuplicate(nums, k, t)) #True





