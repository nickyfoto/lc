#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/
#
# algorithms
# Easy (63.21%)
# Total Accepted:    4.7K
# Total Submissions: 7.4K
# Testcase Example:  '["cbd"]\n["zaaaz"]'
#
# Let's define a function f(s) over a non-empty string s, which calculates the
# frequency of the smallest character in s. For example, if s = "dcce" then
# f(s) = 2 because the smallest character is "c" and its frequency is 2.
# 
# Now, given string arrays queries and words, return an integer array answer,
# where each answer[i] is the number of words such that f(queries[i]) < f(W),
# where W is a word in words.
# 
# 
# Example 1:
# 
# 
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so
# f("cbd") < f("zaaaz").
# 
# 
# Example 2:
# 
# 
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second
# query both f("aaa") and f("aaaa") are both > f("cc").
# 
# 
# 
# Constraints:
# 
# 
# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] are English lowercase letters.
# 
# 
#
class Solution:
    # def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    def numSmallerByFrequency(self, queries, words):
        # print(ord('a'), ord('c'))
        def f(q):
            l = sorted(list(q))
            return l.count(l[0])
        q = list(map(f, queries))
        w = list(map(f, words))
        return [len([y for y in w if y > x]) for x in q]

# s = Solution()
# queries = ["cbd"]
# words = ["zaaaz"]
# print(s.numSmallerByFrequency(queries, words))

# queries = ["bbb","cc"]
# words = ["a","aa","aaa","aaaa"]
# print(s.numSmallerByFrequency(queries, words))
