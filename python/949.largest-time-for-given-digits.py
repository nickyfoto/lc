#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (33.67%)
# Total Accepted:    8.4K
# Total Submissions: 24.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of 4 digits, return the largest 24 hour time that can be
# made.
# 
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
# 
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4]
# Output: "23:41"
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,5,5,5]
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# A.length == 4
# 0 <= A[i] <= 9
# 
# 
# 
#
class Solution:
    # def largestTimeFromDigits(self, A: List[int]) -> str:
    def largestTimeFromDigits(self, A, debug=False):
        # A.sort()
        # at least one element <= 2
        if min(A) > 2:
            return ""

        def update(A, start, res):
            for i in range(start, -1, -1):
                if i in A:
                    res += str(i)
                    A.remove(i)
                    break
            return A, res
        def recur(A, idx, res):
            if idx == 0:
                for i in range(2, -1, -1):
                    if i in A:
                        if i == 2:
                            # if A.count(2) > 1 or A.count(3) > 0 or A.count(1) > 0 or A.count(0) > 0:
                            # print('here') if debug else None
                            if len([x for x in A if x < 6]) > 2:
                                res += str(i)
                                # print('res', res) if debug else None
                                A.remove(i)
                                break
                                # print('len', [x for x in A if x < 6]) if debug else None
                        else:
                            res += str(i)
                            A.remove(i)
                            break
                if len(A) == 4:
                        return ""
                print(0, res) if debug else None
                return recur(A, 1, res)
            elif idx == 1:
                if all([x > 5 for x in A]):
                    return ""
                if res[0] == '2':
                    if all([x > 3 for x in A]):
                        return ""
                    for i in range(3, -1, -1):
                        if i in A:
                            if [x for x in A if x < 6 and x != i] or A.count(i) > 1:
                                res += str(i)
                                A.remove(i)
                                break
                    # print(A)
                    if len(A) == 3:
                        return ""
                    print(1, res) if debug else None
                    return recur(A, 2, res)
                else:
                    # res[0] == '1' or res[0] == '0'
                    for i in range(9, -1, -1):
                        if i in A:
                            # if only 1 element less than 6
                            # keep this element for idx 3 use
                            if i < 6:
                                # if there's still other element less than 6 and not equal to i exists in A
                                # or there's more than one i in A
                                if [x for x in A if x < 6 and x != i] or A.count(i) > 1:
                                    res += str(i)
                                    A.remove(i)
                                    break
                            else:
                                res += str(i)
                                A.remove(i)
                                break
                    if len(A) == 3:
                        return ""
                    print(1, res) if debug else None
                    return recur(A, 2, res)
            elif idx == 2:
                res += ":"
                print(2, res) if debug else None
                return recur(A, 3, res)
            elif idx == 3:
                for i in range(5, -1, -1):
                    if i in A:
                        res += str(i)
                        A.remove(i)
                        break
                if len(A) == 2:
                    return ""
                print(3, res) if debug else None
                return recur(A, 4, res)
            else:
                # for i in range(9, -1, -1):
                #     if i in A:
                #         res += str(i)
                #         A.remove(i)
                #         break
                res += str(A[0])
                print(4, res) if debug else None
                return res

        return recur(A, 0, "")
































