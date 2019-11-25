#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (49.46%)
# Total Accepted:    425.6K
# Total Submissions: 859.6K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

def FastSelect(a, k):
    # median is defined as ceiling(n/2)
    # 1. break a into ceiling n/5 groups
    # 2. for i = 1 ... n/5 sort group[i], let mi = median(Gi)
    # 3. Let s = {m1, m2...m n/5}
    # 4. find the median p of s recursively call p = FastSelect(s, n/10)
    # 5. partition A into A < p, A = p and A > p
    # if k < |a<p| then return FastSelect(A<p, k)
    # if k > |a<p|+|a=p| then return FastSelect(A>p, k-|a<p|-|a=p|)
    # else return p
    n = len(a)
    if n < 6:
        return sorted(a)[k-1]
    groups = [a[x:x+5] for x in range(0,n,5)]
    s = [sorted(g)[len(g)//2] for g in groups]
    print(s, n//10)
    p = FastSelect(s, n//10)
    small = [i for i in a if i < p]
    equal = [i for i in a if i == p]
    big = [i for i in a if i > p]
    if k <= len(small):
        return FastSelect(small, k)
    elif k > len(small) + len(equal):
        return FastSelect(big, k-len(small) - len(equal))
    else:
        return p



class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    def findKthLargest(self, nums, k: int) -> int:

        def FastSelect(a, k):
            n = len(a)
            if n < 6:
                return sorted(a)[k-1]
            groups = [a[x:x+5] for x in range(0,n,5)]
            s = [sorted(g)[len(g)//2] for g in groups]
            # print(s, n//10)
            p = FastSelect(s, n//10)
            small = [i for i in a if i < p]
            equal = [i for i in a if i == p]
            big = [i for i in a if i > p]
            if k <= len(small):
                return FastSelect(small, k)
            elif k > len(small) + len(equal):
                return FastSelect(big, k-len(small) - len(equal))
            else:
                return p
        return FastSelect(nums, len(nums)-k+1)

# s = Solution()
# nums = [3,2,1,5,6,4]
# k = 2
# # print(FastSelect(nums, len(nums)-k+1))
# print(s.findKthLargest(nums, k))
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
# print(s.findKthLargest(nums, k))
# print(FastSelect(nums, len(nums)-k+1))
