#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (37.40%)
# Total Accepted:    131.5K
# Total Submissions: 349.6K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
from collections import Counter
class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    """
    def findAnagrams(self, s, p):
        # Counter('cba') == Counter('abc')
        pl = len(p)
        n = len(s)
        p = Counter(p)
        res = []
        for i in range(n):
            if Counter(s[i:i+pl]) == p:
                res.append(i)
        return res
    """
    def findAnagrams(self, s, p):
        pl = len(p)
        pc = Counter(p)
        ps = Counter(s[:pl])
        res = []
        n = len(s)
        match = False
        if ps == pc:
            res.append(0)
            match = True
        for i in range(pl, n):
            if match:
                if s[i-pl] == s[i]:
                    res.append(i-pl+1)
                    # print(s[i-pl], s[i], res)
                else:
                    ps[s[i-pl]] -= 1
                    if ps[s[i-pl]] == 0:
                        del ps[s[i-pl]]
                    if s[i] not in ps:
                        ps[s[i]] = 1
                    else:
                        ps[s[i]] += 1
                    # print(s[i-pl], s[i], ps, res)
                    match = False
            else:
                if s[i-pl] == s[i]:
                    pass
                    # print('pass', s[i-pl], s[i], ps, res)
                else:
                    ps[s[i-pl]] -= 1
                    if ps[s[i-pl]] == 0:
                        del ps[s[i-pl]]
                    if s[i] not in ps:
                        ps[s[i]] = 1
                    else:
                        ps[s[i]] += 1
                    if ps ==pc:
                        res.append(i-pl+1)
                        match = True
                    # print('not equal', s[i-pl], s[i], ps, res)



        return res

# S = Solution()
# s, p = "cbaebabacd", "abc"
# print(S.findAnagrams(s, p))

# s, p = "abab", "ab"
# print(S.findAnagrams(s, p))





























        
