#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (44.31%)
# Total Accepted:    35.1K
# Total Submissions: 78.6K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
# 
# Example 1:
# 
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
# 
# 
# 
# Example 2:
# 
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
# 
#

class Node:
    def __init__(self, R):
        self.next = [None] * R
        self.val = 0

class TrieST(object):

    def __init__(self, R):
        self.R = R
        self.root = None

    """docstring for TrieST"""
    def _put(self, x, key, val, d):
        # print('key=', key, 'd=', d, 'val=', val)
        if not x:
            x = Node(self.R)
        if d == len(key):
            x.val = val
            return x
        c = key[d]
        x.next[ord(c)] = self._put(x.next[ord(c)], key, val, d+1)
        # print('here', x[ord(c)])
        # print('here val=', val)
        return x
    def put(self, key, val=None):
        self.root = self._put(self.root, key, val, 0)

    def _get(self, x, key, d):
        if d == len(key):
            return x
        c = key[d]
        return self._get(x.next[ord(c)], key, d+1)
    def get(self, key):
        # print('get root', self.root)
        x = self._get(self.root, key, 0)
        return x.val

st = TrieST(256)
st.put('community', 1)
st.get('cmm')
class Solution:
    # def longestWord(self, words: List[str]) -> str:
    # def longestWord(self, words):
    #     st = TrieST(256)
    #     for w in words:
    #         st.put(w, 1)
    #     scores = [] 
    #     for w in words:
    #         score = 0
    #         # print('word=', w)
    #         for i in range(len(w)):
    #             # print(w[:i+1], st.get(w[:i+1]))
    #             s = st.get(w[:i+1])
    #             if len(w) > 1 and s == 0:
    #                 score = 0
    #                 break
    #             else:
    #                 score += s
    #         # print(w, 'total=', score)
    #         # print('='*30)
    #         scores.append(score)
    #     # print(scores)
    #     max_score = max(scores)
    #     if max_score == 0:
    #         return ""
    #     candidates = [words[i] for i in range(len(words)) if scores[i] == max_score]
    #     candidates.sort()
    #     # print(len(candidates), len(set(candidates)))
    #     return candidates[0]

    
    def longestWord(self, words):
        words.sort(reverse=True, key=lambda s: len(s))
        st = TrieST(256)
        for w in words:
            st.put(w, 1)
        # scores = []
        # max_word_length = len(words[0]) 
        # c2 = []
        def getScore(w):
            score = 0
            for i in range(len(w)):
                # print(w[:i+1], st.get(w[:i+1]))
                s = st.get(w[:i+1])
                if len(w) > 1 and s == 0:
                    score = 0
                    break
                else:
                    score += s
            return score
        i = 0
        # print(words)
        while i < len(words):
            l = len(words[i])
            candidates = []
            if getScore(words[i]) == l:
                candidates.append(words[i])
                while i + 1 < len(words) and len(words[i+1]) == l:
                # print('i=', i, words[i], getScore(words[i]))
                    if getScore(words[i+1]) == l:
                        candidates.append(words[i+1])
                    i += 1
                # s = getScore(words[i-1])
                # print('i=', i, words[i], getScore(words[i]), candidates)
                if candidates:
                    # print(words[i-1], s)
                    # print(candidates)
                    candidates.sort()
                    # print(len(candidates[0]))
                    return candidates[0]
            i += 1
        return ""
        # print(words[i])




# s = Solution()



















