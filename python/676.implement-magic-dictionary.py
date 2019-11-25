#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#
# https://leetcode.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (52.12%)
# Total Accepted:    28.5K
# Total Submissions: 54.7K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 
# Implement a magic directory with buildDict, and search methods.
# 
# 
# 
# For the method buildDict, you'll be given a list of non-repetitive words to
# build a dictionary.
# 
# 
# 
# For the method search, you'll be given a word, and judge whether if you
# modify exactly one character into another character in this word, the
# modified word is in the dictionary you just built.
# 
# 
# Example 1:
# 
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# 
# 
# 
# Note:
# 
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think
# about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class
# MagicDictionary, as static/class variables are persisted across multiple test
# cases. Please see here for more details.
# 
# 
#
class Node:
    def __init__(self, R):
        self.next = [None] * R
        self.val = None

    
        

    

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.R = 256
        self.root = None
        
    def minus97(self, c):
        return ord(c) - 97

    def put(self, x, key, val, d):
        if not x:
            x = Node(self.R)
        if d == len(key):
            x.val = val
            return x
        c = key[d]
        # print(c, key)
        x.next[self.minus97(c)] = self.put(x.next[self.minus97(c)], key, val, d+1)
        return x

    # def buildDict(self, dict: List[str]) -> None:
    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.root = self.put(self.root, key=word, val=1, d=0)

    def _get(self, x, key, d):
        if d == len(key):
            return x
        c = key[d]
        if x:
            return self._get(x.next[self.minus97(c)], key, d+1)
        else:
            return None

    def get(self, key):
        # print('get root', self.root)
        x = self._get(self.root, key, 0)
        if x:
            return x.val
        else:
            return None
    
    def keys_that_match(self, pattern, word):
        result = []
        self.collect(self.root, "", pattern, result, word)
        return result

    def collect(self, node, prefix, pattern, result, word):
        if not node:
            return None
        d = len(prefix)
        if d == len(pattern) and node.val != None:
            result.append(prefix)
        if d == len(pattern):
            return
        c = pattern[d]
        if c == '.':
            for i in range(26):
                # print(word[d])
                if i != self.minus97(word[d]):
                    prefix += chr(i+97)
                    self.collect(node.next[i], prefix, pattern, result, word)
                    prefix = prefix[:-1]
        else:
            prefix += c
            self.collect(node.next[self.minus97(c)], prefix, pattern, result, word)
            prefix = prefix[:-1]

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        # if self.get(word):
            # return False
        for i in range(len(word)):
            fuzz = word[:i] + '.' + word[i+1:]
            # print(fuzz, self.keys_that_match(fuzz))
            results = self.keys_that_match(fuzz, word)
            # if results:
                # if word in results:
                    # return False
            # print(word, results)
            if results:
                print(results)
                return True
        return False
            # if self.get(fuzz):
                # return True

# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
# obj.buildDict(["hello","leetcode"])
# print(obj.search("hello")) # False
# # print(obj.search("hhllo")) # True
# # print(obj.search("hell"))# Output: False
# # print(obj.search("leetcoded"))# Output: False
words = ["hello","hallo","leetcode"]
obj.buildDict(words)
# print(obj.search("hello")) # True
# print(obj.search("hello")) # True
print(obj.search("hvllo")) # True