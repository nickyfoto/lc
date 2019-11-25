#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (54.25%)
# Total Accepted:    16.1K
# Total Submissions: 29.5K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# 
# Return the length of the longest (contiguous) subarray that contains only
# 1s. 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# Example 2:
# 
# 
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1 
# 
# 
# 
# 
#
class Solution:
    # def longestOnes(self, A: List[int], K: int) -> int:
    def zeroK(self, A):
        n = len(A)
        max_ones = 0
        i = 0
        while i < n:
            if A[i] == 1:
                num_of_ones = 0
                while i < n and A[i] == 1:
                    num_of_ones += 1
                    i += 1
                # print('i=', i, 'num_of_ones=', num_of_ones)
                if num_of_ones > max_ones:
                    max_ones = num_of_ones
            i += 1 
        return max_ones

    def longestOnes2(self, A, K):
        if K == 0:
            return self.zeroK(A)
        n = len(A)
        left = 0
        max_ones = 0
        while left < n:
            i = left
            num_of_zeros = 0
            while i < n:
                if A[i] == 0:
                    num_of_zeros += 1
                    if num_of_zeros > K:
                        break
                i += 1
            total = i - left
            if total > max_ones:
                max_ones = total
            left += 1
            if max_ones:
                if n - left < max_ones:
                    break
        return max_ones

    def longestOnes(self, A, K):
        if K == 0:
            return self.zeroK(A)
        n = len(A)
        # print(n)
        left = 0
        max_ones = 0
        i = 0
        num_of_zeros = 0
        num_of_ones = 0
        while left < n and i < n:
            if A[i]:
                num_of_ones += 1
            else:
                num_of_zeros += 1
            if num_of_zeros > K:
                # print('here, i=', i, 'left=', left)
                # print('num_of_zeros=', num_of_zeros)
                # print('num_of_ones=', num_of_ones)

                total = num_of_zeros - 1 + num_of_ones
                # print('total=', total)
                
                if total > max_ones:
                    max_ones = total
                # print('max_ones=', max_ones)
                # print('='*20)

                while num_of_zeros > K:
                    if A[left] == 0:
                        num_of_zeros -= 1
                        left += 1
                    else:
                        num_of_ones -= 1
                        left += 1
            i += 1
        # print('num_of_ones=', num_of_ones, 'num_of_zeros=', num_of_zeros)
        # print('total=', total)
        # print('i=', i, 'left=', left)
        total = num_of_ones + num_of_zeros
        if total > max_ones:
            max_ones = total
        return max_ones



# s = Solution()
# A = [1,1,1,0,0,0,1,1,1,1,0]
# K = 2
# print(s.longestOnes(A, K) == 6)


# A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# K = 3
# print(s.longestOnes(A, K)== 10)

# A = [0,0,1,1,1,0,0]
# K = 0
# print(s.longestOnes(A, K) == 3)

# A = [1,1,1,0,0,0,1,1,1,1]
# K = 0
# print(s.longestOnes(A, K) == 4)

# A = [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1]
# K = 8
# print(s.longestOnes(A, K) == 25)
# # print(s.longestOnes(A, K))


# A = [1,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1]
# K = 10
# print(s.longestOnes(A, K) == 30)


