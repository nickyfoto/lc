#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#
# https://leetcode.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (31.44%)
# Total Accepted:    70.2K
# Total Submissions: 222.9K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# Given two strings A and B, find the minimum number of times A has to be
# repeated such that B is a substring of it. If no such solution, return -1.
# 
# For example, with A = "abcd" and B = "cdabcdab".
# 
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a
# substring of it; and B is not a substring of A repeated two times
# ("abcdabcd").
# 
# Note:
# The length of A and B will be between 1 and 10000.
# 
#
from collections import Counter
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B in A:
            return 1
        cb = Counter(B)
        for k in cb:
            if k not in A:
                return -1
        if len(B) <= len(A):
            A = list(A)
            for i in range(1, len(A)):
                if B[0] == A[i]:
                    if B in "".join(A[i:] + A[:i]):
                        return 2
            return -1
        else:
            la = len(A)
            i = 0
            while i < la:
                temp = A
                while i < la and B[:la] != temp:
                    i += 1
                    temp = A[i:] + A[:i]
                if i == la:
                    return -1
                if i == 0:
                    count = 1
                    B = B[la:]
                else:
                    count = 2
                    B = B[2*la-i:]
                while len(B) >= la and B[:la] == A:
                    B = B[la:]
                    count += 1
                if not B:
                    return count
                elif B == A[:len(B)]:
                    return count + 1
                i += 1
                

# s = Solution()
# A = 'a'
# B = 'aa'
# # # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == 2)


# A = "bb"
# B = "bbbbbbb"
# # # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == 4)

# A = 'abcd'
# B = "cdabcdab"
# # # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == 3)


# A = "abc"
# B = "cabcabca"
# # # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == 4)

# A = "abcd"
# B = "abcdb"
# # # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == -1)

# # # baabaa

# A = "baa"
# B = "abaab"
# # # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == 3)

# A = "abaabaa"
# B = "abaababaab"
# # # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == -1)

# A = "abccb"
# B = "cbabccb"
# # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == 2)

# A = "abcd"
# B = "cdabcdacdabcda"
# # print(s.repeatedStringMatch(A, B))
# print(s.repeatedStringMatch(A, B) == -1)
