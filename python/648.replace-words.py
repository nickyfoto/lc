#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (52.91%)
# Total Accepted:    38.4K
# Total Submissions: 72.5K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
# 
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
# 
# You need to output the sentence after the replacement.
# 
# Example 1:
# 
# 
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# 
# 
# 
# 
# Note:
# 
# 
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000
# 
# 
# 
# 
#
from collections import Counter
class Solution:
    # def replaceWords(self, dict: List[str], sentence: str) -> str:
    def replaceWords(self, dict, sentence) -> str:
        l = list(map(len, dict))
        # print(list(l))
        min_length, max_length = min(l), max(l)
        # print(min_length, max_length)
        s = sentence.split()
        # print(s)
        d = Counter(dict)
        for word in range(len(s)):
            for r in range( min_length, max_length+1):
                if s[word][:r] in d:
                    s[word] = s[word][:r]
                    break
                # print(r)
        # print(s)
        return " ".join(s)


# s = Solution()
# dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# print(s.replaceWords(dict, sentence))

# dict = ["a", "aa", "aaa", "aaaa"]
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# print(s.replaceWords(dict, sentence))


 # ✘ answer: "a aa a aaaa aaa aaa aaa aaaa bbb baba a"
  # ✘ expected_answer: "a a a a a a a a bbb baba a"
