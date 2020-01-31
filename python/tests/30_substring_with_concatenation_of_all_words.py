#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (24.64%)
# Likes:    711
# Dislikes: 1090
# Total Accepted:    159.5K
# Total Submissions: 646.8K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict
from string import ascii_lowercase
class Solution:
    def findSubstring_me(self, s, words):
        if not s or not words:
            return []
        words_length = sum(map(len, words))
        # print(len(s))
        if len(s) < words_length:
            return []
        
        unit_length = len(words[0])
        # print(words_length)
        l = 0
        r = words_length
        res = []

        letter_count = {k:0 for k in ascii_lowercase}
        letter_count.update(Counter("".join(words)))
        
        s_count = {k:0 for k in ascii_lowercase}
        s_count.update(Counter(s[:r]))
        letter_same_count = sum([letter_count[k] == s_count[k] for k in letter_count])
        c = Counter(words)
        
        def valid(s):
            return Counter([s[i*unit_length:unit_length * (i + 1)] for i in range(len(words))]) == c
        # print()
        # print({k: v for k, v in letter_count.items() if v != 0})
        while r <= len(s):
            if letter_same_count == 26:
                if valid(s[l:r]):
                    res.append(l)
                    while len(Counter(s[l:unit_length])) > 1 and r < len(s) and s[l:unit_length] == s[r:r+unit_length]:
                        l += unit_length
                        r += unit_length
                        res.append(l)
                        # print('here', res)
            # print('l=', l, 'r=', r, letter_same_count)
            # print({k: v for k, v in s_count.items() if v != 0})
            if r == len(s):
                break
            if letter_count[s[l]] == s_count[s[l]]:
                letter_same_count -= 1
            
            s_count[s[l]] -= 1
            
            if letter_count[s[l]] == s_count[s[l]]:
                letter_same_count += 1

            if letter_count[s[r]] == s_count[s[r]]:
                letter_same_count -= 1

            s_count[s[r]] += 1
            
            if letter_count[s[r]] == s_count[s[r]]:
                letter_same_count += 1
            l += 1
            r += 1
            # print(r, len(s))

        # print(res)
        return res
    def findSubstring(self, s, words):
        wordBag = Counter(words)   # count the freq of each word
        wordLen, numWords = len(words[0]), len(words)
        totalLen, res = wordLen*numWords, []
        for i in range(len(s)-totalLen+1):   # scan through s
            # For each i, determine if s[i:i+totalLen] is valid
            seen = defaultdict(int)   # reset for each i
            for j in range(i, i+totalLen, wordLen):
                currWord = s[j:j+wordLen]
                if currWord in wordBag:
                    seen[currWord] += 1
                    if seen[currWord] > wordBag[currWord]:
                        break
                else:   # if not in wordBag
                    break    
            if seen == wordBag:
                res.append(i)   # store result
        return res
# @lc code=end
