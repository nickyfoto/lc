#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (56.42%)
# Total Accepted:    69.4K
# Total Submissions: 123K
# Testcase Example:  '[1,2,3,4]'
#
# A sequence of number is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
# 
# For example, these are arithmetic sequence:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# The following sequence is not arithmetic. 1, 1, 2, 5, 7 
# 
# 
# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 
# 
# A slice (P, Q) of array A is called arithmetic if the sequence:
# ⁠   A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this
# means that P + 1 < Q.
# 
# The function should return the number of arithmetic slices in the array A. 
# 
# 
# Example:
# 
# A = [1, 2, 3, 4]
# 
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.
# 
#
class Solution:
    # def numberOfArithmeticSlices(self, A: List[int]) -> int:
    def numberOfArithmeticSlices(self, A):


        def count(length):
            # count how many arithmetic slices in given length
            if length == 3:
                return 1
            else:
                return length - 2 + count(length-1)
        # print(count(3))
        # print(count(4))
        # print(count(5))
        # print(count(6))

        n = len(A)


        lst = []

        i = 0
        while i + 2 < n:
            j = i+1
            k = j+1
            if A[k]-A[j] == A[j]-A[i]:
                start = i
                while A[k]-A[j] == A[j]-A[i]:
                    i += 1
                    j = i+1
                    k = j+1
                    if k > n-1:
                        break
                # print(start, k)
                length = k - start
                lst.append(length)
            i += 1
        # print(length)
        # print(count(length))
        # print(length)
        return sum(map(count, lst))





# s = Solution()
# A = [1,2,3,4]
# print(s.numberOfArithmeticSlices(A))
        
# A = [1, 3, 5, 7, 9]
# print(s.numberOfArithmeticSlices(A))

# A = [1, 1, 2, 5, 7]
# print(s.numberOfArithmeticSlices(A))

# A = [7, 7, 7, 7]
# print(s.numberOfArithmeticSlices(A))

# A = [3, -1, -5, -9]
# print(s.numberOfArithmeticSlices(A))

# A = [0, 3, -1, -5, -9, 0, 1, 3, 5, 7, 9]
# print(s.numberOfArithmeticSlices(A))


















