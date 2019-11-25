#
# @lc app=leetcode id=1053 lang=python3
#
# [1053] Previous Permutation With One Swap
#
# https://leetcode.com/problems/previous-permutation-with-one-swap/description/
#
# algorithms
# Medium (46.86%)
# Total Accepted:    6.4K
# Total Submissions: 13.6K
# Testcase Example:  '[3,2,1]'
#
# Given an array A of positive integers (not necessarily distinct), return the
# lexicographically largest permutation that is smaller than A, that can be
# made with one swap (A swap exchanges the positions of two numbers A[i] and
# A[j]).  If it cannot be done, then return the same array.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,2,1]
# Output: [3,1,2]
# Explanation: Swapping 2 and 1.
# 
# 
# Example 2:
# 
# 
# Input: [1,1,5]
# Output: [1,1,5]
# Explanation: This is already the smallest permutation.
# 
# 
# Example 3:
# 
# 
# Input: [1,9,4,6,7]
# Output: [1,7,4,6,9]
# Explanation: Swapping 9 and 7.
# 
# 
# Example 4:
# 
# 
# Input: [3,1,1,3]
# Output: [1,3,1,3]
# Explanation: Swapping 1 and 3.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# 1 <= A[i] <= 10000
# 
# 
#
class Solution:
    # def prevPermOpt1(self, A: List[int]) -> List[int]:
    def prevPermOpt2(self, A):
        # A = tuple(A)

        n = len(A)
        if n == 1:
            return A
        
        if n == 2:
            if A[1] < A[0]:
                return [A[1], A[0]]
            else:
                return A




        def find_idx(A, target):
            res = self.prevPermOpt1(A)
            # print('here', A, res, target)
            if res == A:
                if A[-1] < target:
                    return len(A) - 1
                else:
                    return None
            else:
                return find_idx2(A, target)
                # todo

        def find_idx2(A, target):
            # find max that less than target
            # print('here',A, target)
            n = len(A)
            i = 1
            mx = A[0]
            mx_idx = 0
            while i < n:
                if A[i] < target:
                    if A[i] > mx:
                        mx = A[i]
                        mx_idx = i
                i += 1
            # print(mx_idx)
            return mx_idx


        if A[0] == max(A) and A[1:] == self.prevPermOpt1(A[1:].copy()):
            # print('here')
            idx = find_idx2(A[1:], target=A[0])
            A = A.copy()
            A[0], A[idx+1] = A[idx+1], A[0]
            return A


        def process(A):
            idx = find_idx(A[1:], target=A[0])
            # print(A, idx)
            # print(A, idx)
            if idx != None:
                # print(idx)
                A[0], A[idx+1] = A[idx+1], A[0]
                # print(A)
                return A
            else:
                return None


            return A



        # print('A=', A)




        i = 0
        while i < n:
            j = i+1
            while j < n and i < n and A[j] >= A[i]:
                i += 1
                j += 1
            if j == n:
                return A

            else:
                if i == 0:
                    # print(i,j, A)
                    res = process(A[j:].copy())
                    if res:
                        A = A.copy()
                        A[j:] = res
                    else:
                        while j > 1 and not res:
                            j -= 1
                            res = process(A[j:].copy())
                        if not res:
                            todo
                        else:
                            A = A.copy()
                            A[j:] = res
                            return A
                else:
                    # print('here')
                    res = process(A[i:].copy())
                    if res:
                        A = A.copy()
                        A[i:] = res
                    else:
                        todo
                    
                return A

    def prevPermOpt1(self, A):
        A = tuple(A)
        
        n = len(A)
        if n == 1:
            return list(A)
        
        if n == 2:
            if A[1] < A[0]:
                return [A[1], A[0]]
            else:
                return list(A)

        def find_idx(A, target):
            # find max that less than target
            # print('here',A, target)
            n = len(A)
            i = 1
            mx = A[0]
            mx_idx = 0
            while i < n:
                if A[i] < target:
                    if A[i] > mx:
                        mx = A[i]
                        mx_idx = i
                i += 1
            # print(mx_idx)
            return mx_idx


        def is_non_decreasing(A):
            for i in range(1, len(A)):
                if A[i-1] > A[i]:
                    return False
            return True

        # is_non_decreasing(A[1:])
        # if A[0] == max(A) and A[1:] == tuple(self.prevPermOpt1(A[1:])):
        if A[0] == max(A) and is_non_decreasing(A[1:]):
            idx = find_idx(A[1:], target=A[0])
            A = list(A)
            A[0], A[idx+1] = A[idx+1], A[0]
            return A


        def process(A):
            idx = find_idx(A[1:], target=A[0])
            A = list(A)
            A[0], A[idx+1] = A[idx+1], A[0]
            return A
            



        # print('A=', A)




        i = 0
        while i < n:
            j = i+1
            while j < n and i < n and A[j] >= A[i]:
                i += 1
                j += 1
            if j == n:
                return list(A)

            else:
                if i == 0:
                    # print(i,j, 'asking prevPermOpt1', A[j:])
                    # res = self.prevPermOpt1(A[j:])
                    if A[j:][0] > max(A[j:][1:]):
                        print('logic wrong')
                        print('only when cannot swap smaller digit')
                        print('we swap larget digit')
                        res = process(A[j:])
                        A = list(A)
                        A[j:] = res
                    else:
                        print(A[j:][1:], 'does not have element smaller than', A[j:][0])
                        # res = self.prevPermOpt1(A[j:])
                        # print('input', A[j:], 'res=', res)
                    # print('input=', A[j:], 'res=', res)
                    # if res:
                        
                    # else:
                    #     while j > 1 and not res:
                    #         j -= 1
                    #         res = process(A[j:].copy())
                    #     if not res:
                    #         todo
                    #     else:
                    #         A = A.copy()
                    #         A[j:] = res
                    #         return A
                else:
                    # print('here')
                    res = process(A[i:])
                    if res:
                        A = list(A)
                        A[i:] = res
                    # else:
                        # todo
                    
                return A

    def prevPermOpt1(self, A):
        n = len(A)

        def find_idx(A, target):
            # find max that less than target
            # print('here',A, target)
            n = len(A)
            i = 1
            mx = A[0]
            mx_idx = 0
            while i < n:
                if A[i] < target:
                    if A[i] > mx:
                        mx = A[i]
                        mx_idx = i
                i += 1
            # print(mx_idx)
            return mx_idx


        for i in range(n - 1, 0, -1):
            if A[i-1] > A[i]:
                arr = A[i:]
                idx = find_idx(arr, target=A[i-1])
                A[i-1], A[i+idx] = arr[idx], A[i-1]
                return A
        # print(mx, mx_idx)
        return A

# s = Solution()
# A = [1,1,5]
# print(s.prevPermOpt1(A) == A)

# A = [1]
# print(s.prevPermOpt1(A) == A)

# A = [1,1]
# print(s.prevPermOpt1(A) == A)

# A = [1,2]
# print(s.prevPermOpt1(A) == A)

# A = [2,1]
# print(s.prevPermOpt1(A) == [1,2])

# A = [1,1,1]
# print(s.prevPermOpt1(A) == A)

# A = [3,2,1]
# print(s.prevPermOpt1(A) == [3,1,2])

# A = [1,9,4,6,7]
# print(s.prevPermOpt1(A) == [1,7,4,6,9])

# A = [3,1,1,3]
# # print(s.prevPermOpt1(A))
# print(s.prevPermOpt1(A) == [1,3,1,3])
        
# A = [1,2,3,4,5]
# print(s.prevPermOpt1(A) == [1,2,3,4,5])

# A = [5,4,3,2,1]
# print(s.prevPermOpt1(A) == [5,4,3,1,2])


# A = [2,1,2,1,1,2,2,1]
# print(s.prevPermOpt1(A) == [2,1,2,1,1,2,1,2])
