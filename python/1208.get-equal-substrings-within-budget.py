#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
#
# algorithms
# Medium (34.25%)
# Total Accepted:    5.3K
# Total Submissions: 15.6K
# Testcase Example:  '"abcd"\n"bcdf"\n3'
#
# You are given two strings s and t of the same length. You want to change s to
# t. Changing the i-th character of s to i-th character of t costs |s[i] -
# t[i]| that is, the absolute difference between the ASCII values of the
# characters.
# 
# You are also given an integer maxCost.
# 
# Return the maximum length of a substring of s that can be changed to be the
# same as the corresponding substring of t with a cost less than or equal to
# maxCost.
# 
# If there is no substring from s that can be changed to its corresponding
# substring from t, return 0.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum
# length is 3.
# 
# Example 2:
# 
# 
# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to charactor in t, so the
# maximum length is 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You can't make any change, so the maximum length is 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 10^5
# 0 <= maxCost <= 10^6
# s and t only contain lower case English letters.
# 
# 
#
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        diff = [abs(ord(x)-ord(y)) for x,y in zip(s, t)]
        # print(diff)

        if maxCost == 0:
            return diff.count(0)


        n = len(s)
        L = [0] * n
        costs = [0] * n
        sliding_window = []
        i = 0
        while i < n:
            if diff[i] > maxCost:
                costs[i] = diff[i]
                L[i] = 0
                sliding_window = [diff[i]]
            else:
                if i == 0:
                    cost = diff[i]
                else:
                    cost = costs[i-1] + diff[i]
                sliding_window.append(diff[i])
                if cost > maxCost:
                    while sliding_window and cost > maxCost:
                        cost -= sliding_window.pop(0)
                costs[i] = cost
                L[i] = len(sliding_window)
            # print('i=', i)
            # print('sliding_window=', sliding_window)
            # print('costs=', costs)
            # print('L=', L)
            # print('='*30)
            i += 1
        return max(L)

# S = Solution()

# s = "abcd"
# t = "bcdf"
# maxCost = 3
# print(S.equalSubstring(s, t, maxCost) == 3)

# s = "abcd"
# t = "cdef"
# maxCost = 3
# print(S.equalSubstring(s, t, maxCost) == 1)

# s = "abcd"
# t = "acde"
# maxCost = 0
# print(S.equalSubstring(s, t, maxCost) == 1)


# s = "krrgw"
# t = "zjxss"
# maxCost = 19
# print(S.equalSubstring(s, t, maxCost) == 2) #2



# s = "anryddgaqpjdw"
# t = "zjhotgdlmadcf"
# maxCost = 5
# print(S.equalSubstring(s, t, maxCost) == 1) #1
