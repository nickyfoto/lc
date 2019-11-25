#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.62%)
# Total Accepted:    26.4K
# Total Submissions: 95.3K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: A = "ab", B = "ba"
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: A = "ab", B = "ab"
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: A = "aa", B = "aa"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: A = "", B = "aa"
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def buddyStrings(self, A: str, B: str) -> bool:

    def buddyStrings(self, A, B):

        def getPosD(s):
            d = {}
            for i in range(len(s)):
                if s[i] not in d:
                    d[s[i]] = [i]
                else:
                    d[s[i]].append(i)
            return d

        la = len(A)
        lb = len(B)
        if la != lb:
            return False
        diff_a = []
        diff_b = []
        for i in range(la):
            if A[i] != B[i]:
                diff_a.append(A[i])
                diff_b.append(B[i])
        # print(diff_a, diff_b)
        if not diff_a or not diff_b:
            da = getPosD(A)
            db = getPosD(B)
            if da == db and [v for k, v in da.items() if len(v) > 1]:
                return True
            # print([v for k, v in da.items() if len(v) > 1])
            # print(da, db)

            return False
        if diff_b == [diff_a[1], diff_a[0]]:
            return True
        return False
        
# s = Solution()
# A = "ab"
# B = "ba"
# print(s.buddyStrings(A, B))

# A = "ab"
# B = "ab"
# print(s.buddyStrings(A, B))

# A = "aaaaaaabc"
# B = "aaaaaaacb"
# print(s.buddyStrings(A, B))


# A = 'aa'
# B = 'aa'
# print(s.buddyStrings(A, B))