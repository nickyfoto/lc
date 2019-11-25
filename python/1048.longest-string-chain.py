#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (50.38%)
# Total Accepted:    14.2K
# Total Submissions: 28.2K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
# 
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
# 
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
# 
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
# 
# 
# 
# 
# 
#
from collections import defaultdict
class Solution:
    # def longestStrChain(self, words: List[str]) -> int:
    def longestStrChain(self, words) -> int:

        words = list(set(words))

        words.sort(key=len)

        n = len(words)


        def f(word):
            if len(word) > 1:
                return {word[:i] + word[i+1:]: 1 for i in range(len(word)) }
            else:
                return {word: 1}

        word_d = [f(word) for word in words]
        
        # print(word_d)

        i = 0
        p = []
        while i < n:
            length = len(words[i])
            j = i+1
            while j < n and len(words[j]) == length:
                j += 1
            p.append((i,j))
            i = j

        # print(words)
        # print(word_d)
        for i in range(1, len(p)):
            for child in range(*p[i-1]):
                for parent in range(*p[i]):
                    # print(word_d[child], word_d[parent])
                    if words[child] in word_d[parent]:
                        # print(child, words[child], parent, words[parent])
                        # print('here', words[child], word_d[parent], word_d[child])
                        word_d[parent][words[child]] += max(word_d[child].values())
                        # print('after', word_d)
        # print(word_d)

        # print([max(d.values()) for d in word_d])
        return max([max(d.values()) for d in word_d])








# s = Solution()
# words = ["a","b","ba","bca","bda","bdca"]
# print(s.longestStrChain(words) == 4)




# words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
# print(s.longestStrChain(words) == 7)


# # 62/71
# words = ["wnyxmflkf","xefx","usqhb","ttmdvv","hagmmn","tmvv","pttmdvv","nmzlhlpr","ymfk","uhpaglmmnn","zckgh","hgmmn","isqxrk","isqrk","nmzlhpr","uysyqhxb","haglmmn","xfx","mm","wymfkf","tmdvv","uhaglmmn","mf","uhaglmmnn","mfk","wnymfkf","powttkmdvv","kwnyxmflkf","xx","rnqbhxsj","uysqhb","pttkmdvv","hmmn","iq","m","ymfkf","zckgdh","zckh","hmm","xuefx","mv","iqrk","tmv","iqk","wnyxmfkf","uysyqhb","v","m","pwttkmdvv","rnqbhsj"]
# # print(sorted(words, key=len))
# print(s.longestStrChain(words) == 10) # 10



