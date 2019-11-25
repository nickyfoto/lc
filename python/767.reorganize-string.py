#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (43.59%)
# Total Accepted:    33.9K
# Total Submissions: 77.8K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
# 
#
from queue import PriorityQueue
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        pq = PriorityQueue()
        
        def pq_add(k, v):
            pq.put((-v, k))
        
        def pq_get():
            v, k = pq.get()
            return k, -v

        for k in c:
            pq_add(k, c[k])

        # print(pq.queue)

        res = []
        tk, tv = None, 0
        while not pq.empty():
            k, v = pq_get()
            res.append(k)
            v -= 1
            if v > 0:
                if not tk:
                    tk, tv = k, v
                else:
                    pq_add(tk, tv)
                    tk, tv = k, v
            else:
                if tk:
                    pq_add(tk, tv)
                    tk, tv = None, 0
        # print(res, tk, tv)
        if tv > 1:
            return ""
        if tk:
            if tk == res[-1]:
                return ""
            else:
                res.append(tk)
                return "".join(res)
        return "".join(res)


# s = Solution()
# S = ''
# print(s.reorganizeString(S)=='')
# S = 'a'
# print(s.reorganizeString(S)=='a')
# S = 'aa'
# print(s.reorganizeString(S)=='')
# S = "aab"
# print(s.reorganizeString(S)=='aba')
# S = "aabb"
# print(s.reorganizeString(S)=='abab')
# S = "aabba"
# print(s.reorganizeString(S)=='ababa')

# S = 'vvvlo'
# print(s.reorganizeString(S)=='vlvov')
