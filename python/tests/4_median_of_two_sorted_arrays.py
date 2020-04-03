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
    def findMedianSortedArrays2(self, nums1, nums2):


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


    def findMedianSortedArrays(self, nums1, nums2):

        def getKth(nums1, start1, nums2, start2, k):
            if start1 > len(nums1) - 1:
                return nums2[start2 + k - 1]
            if start2 > len(nums2) - 1:
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            mid1 = float('inf')
            mid2 = float('inf')
            if start1 + k // 2 - 1 < len(nums1):
                mid1 = nums1[start1 + k // 2 - 1]
            if start2 + k // 2 - 1 < len(nums2):
                mid2 = nums2[start2 + k // 2 - 1]
            if mid1 < mid2:
                return getKth(nums1, start1 + k // 2, nums2, start2, k - k // 2)
            else:
                return getKth(nums1, start1, nums2, start2 + k // 2, k - k // 2)
        
        n = len(nums1) + len(nums2)
        l = (n + 1) // 2
        r = (n + 2) // 2
        return (getKth(nums1, 0, nums2, 0, l) + getKth(nums1, 0, nums2, 0, r)) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        """
        assume len(nums1) <= len(nums2)

        this is why the problem is hard
        """
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        l, r, half_len = 0, m, (m + n + 1) // 2
        while l <= r:
            mid = l + (r - l) // 2
            j = half_len - mid
            if mid < m and nums2[j - 1] > nums1[mid]:
                l = mid + 1
            elif mid > 0 and nums1[mid - 1] > nums2[j]:
                r = mid - 1
            else:
                if mid == 0: max_left = nums2[j - 1]
                elif j == 0: max_left = nums1[mid - 1]
                else: max_left = max(nums1[mid - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left
                
                if mid == m: min_right = nums2[j]
                elif j == n: min_right = nums1[mid]
                else: min_right = min(nums1[mid], nums2[j])
                return (max_left + min_right) / 2

# @lc code=end
