#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (28.17%)
# Likes:    5761
# Dislikes: 865
# Total Accepted:    578.9K
# Total Submissions: 2.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):


        def single_arr_median(arr):
            if len(arr) % 2 == 1:
                return arr[len(arr) // 2]
            else:
                return (arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) / 2
        if not nums1:
            return single_arr_median(nums2)
        if not nums2:
            return single_arr_median(nums1)


        n = len(nums1) + len(nums2)


        if n == 2:
            return (nums1[0] + nums2[0]) / 2

        if n % 2 == 0:
            c1 = 0
            c2 = 0
            while c1 < len(nums1) and c2 < len(nums2):
                n1 = nums1[c1]
                n2 = nums2[c2]
                
                if c1 + c2 == n // 2 - 1:
                    if c1 == len(nums1) - 1:
                        # print(c1, c2, min([nums1[c1], nums2[c2]]))
                        # todo
                        return (min([nums1[c1], nums2[c2+1]]) + nums2[c2]) / 2
                    elif c2 == len(nums2) - 1:
                        return (min([nums1[c1+1], nums2[c2]]) + nums1[c1]) / 2
                    else:
                        # print('here', max([nums1[c1-1], nums2[c2-1]]), min([nums1[c1],   nums2[c2]]))
                        # todo
                        # print(c1, c2)
                        if min([nums1[c1], nums2[c2]]) == nums1[c1]:
                            return (nums1[c1] + min([nums1[c1+1],   nums2[c2]])) / 2
                        else:
                            return (nums2[c2] + min([nums1[c1],   nums2[c2+1]])) / 2
                
                if n1 <= n2:
                    c1 += 1
                else:
                    c2 += 1
                
                    
            if c1 == len(nums1):
                c2 += n // 2 - (c1+c2)
                # print(nums2[c2], )
                return (nums2[c2] + max([nums1[c1-1], nums2[c2-1]])) / 2
            elif c2 == len(nums2):
                c1 += n // 2 - (c1+c2)
                return (nums1[c1] + max([nums1[c1-1], nums2[c2-1]])) / 2
        else:
            # there are n // 2 number large than median
            # n // 2 smaller than median
            c1 = 0
            c2 = 0

            while c1 < len(nums1) and c2 < len(nums2):
                n1 = nums1[c1]
                n2 = nums2[c2]

                if c1 + c2 == n // 2:
                    # print(c1, c2, n1, n2)
                    return min([nums1[c1], nums2[c2]])

                if n1 <= n2:
                    c1 += 1
                else:
                    c2 += 1
                
            if c1 == len(nums1):
                # print(c2, n // 2 - (c1+c2))
                # todo
                return nums2[c2 + (n // 2 - (c1+c2))]
            elif c2 == len(nums2):
                return nums1[c1 + (n // 2 - (c1+c2))]



# @lc code=end
