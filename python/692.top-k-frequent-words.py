#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (46.86%)
# Total Accepted:    81.6K
# Total Submissions: 173.7K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
# 
# Example 1:
# 
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# 
# Example 2:
# 
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# 
# 
# 
# Follow up:
# 
# Try to solve it in O(n log k) time and O(n) extra space.
# 
# 
#

from collections import Counter
class Solution:
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    def topKFrequent2(self, words, k):

        c = Counter(words)
        words = sorted([[w, c[w]] for w in set(words)], key=lambda x: x[1], reverse=True)
        
        # print(words)
        d = {}
        for key, v in words:
            # print(key, v)
            if v not in d:
                d[v] = [key]
            else:
                d[v].append(key)
            if len(d) > k:
                break
        # print(d)
        # print([c for w,c in words[:k]])
        res = []
        for key in sorted(d.keys(), reverse=True):
            res.extend(sorted(d[key]))
            # print('res', res)
        return res[:k]
            
        # return [w[0] for w in words[:k]]


    def topKFrequent(self, words, k):
        c = Counter(words)
        words = list(c.keys())
        words.sort(key= lambda x: (- c[x], x))
        return words[:k]


# s = Solution()
# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2
# print(s.topKFrequent(words, k))

# k = 3
# print(s.topKFrequent(words, k)) # ["i","love","coding"]

# words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
# k = 4
# print(s.topKFrequent(words, k))

# words = ["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]
# k = 1
# print(s.topKFrequent(words, k))
  # ✘ answer: ["hhqpvvt"]
  # ✘ expected_answer: ["fvvdtpnzx"]


# l = [['i', 2], ['love', 2], ['plpaboutit', 2], ['jnoqzdute', 1], ['c', 1], ['d']]



