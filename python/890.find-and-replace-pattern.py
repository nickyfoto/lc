#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (71.20%)
# Total Accepted:    31.1K
# Total Submissions: 43.6K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# You have a list of words and a pattern, and you want to know which words in
# words matches the pattern.
# 
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
# 
# (Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.)
# 
# Return a list of the words in words that match the given pattern. 
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation,
# since a and b map to the same letter.
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20
# 
# 
# 
#
from collections import Counter
class Solution:
    # def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    def findAndReplacePattern(self, words, pattern):
        c = Counter(pattern).most_common()
        
        def getIdx(s):
            return tuple([i for i in range(len(pattern)) if pattern[i] == s])
        
        self.p = set(zip([ v for (k, v) in c], map(getIdx, [k for (k, v) in c])))

        def match(word):
            wc = Counter(word).most_common()
            
            def getIdxW(s):
                return tuple([i for i in range(len(word)) if word[i] == s])        
            
            return set(zip([ v for (k, v) in wc], map(getIdxW, [k for (k, v) in wc]))) == self.p

        return list(filter(match, words))

# s = Solution()
# # words = ["abc","deq","mee","aqq","dkd","ccc"]
# # pattern = "abb"
# # print(s.findAndReplacePattern(words, pattern))



# words = ["badc","abab","dddd","dede","yyxx"]
# pattern = "baba"
# print(s.findAndReplacePattern(words, pattern))





