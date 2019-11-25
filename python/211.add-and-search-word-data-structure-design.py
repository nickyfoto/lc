#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (31.76%)
# Total Accepted:    128.3K
# Total Submissions: 403.8K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#
class Node:
    def __init__(self, c):
        self.c = c
        self.left = None
        self.right = None
        self.mid = None
        self.val = None

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None    

    def put(self, node, key, val, d):
        c = key[d]
        if not node:
            node = Node(c)
        if c < node.c:
            node.left = self.put(node.left, key, val, d)
        elif c > node.c:
            node.right = self.put(node.right, key, val, d)
        elif d < len(key) - 1:
            node.mid = self.put(node.mid, key, val ,d+1)
        else:
            node.val = val
        return node

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        key = word
        val = 1
        self.root = self.put(self.root, key, val, d=0)

    def get(self, node, key, d):
        if not node:
            return None
        c = key[d]
        if c < node.c:
            return self.get(node.left, key, d)
        elif c > node.c:
            return self.get(node.right, key, d)
        elif d < len(key) - 1:
            return self.get(node.mid, key, d+1)
        else:
            return node



    def keysThatMatch(self, pattern):
        result = []
        self.collect(self.root, "", 0, pattern, result)
        return result

    def collect(self, node, prefix, i, pattern, result):
        if not node:
            return
        c = pattern[i]
        if c == '.' or c < node.c:
            self.collect(node.left, prefix, i, pattern, result)
        if c == '.' or c == node.c:
            if i == len(pattern) - 1 and node.val != None:
                result.append(prefix + node.c)
            if i < len(pattern) - 1:
                self.collect(node.mid, prefix + node.c, i+1, pattern, result)
                prefix = prefix[:-1]
        if c == '.' or c > node.c:
            self.collect(node.right, prefix, i, pattern, result)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if '.' in word:
            return self.keysThatMatch(word) != []
        key = word
        node = self.get(self.root, key, 0)
        if not node:
            return False
        # print(node.val)
        if not node.val:
            return False
        else:
            return True


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))# -> false
# print(obj.search("bad"))# -> true
# print(obj.search(".ad"))# -> true
# print(obj.search("b.."))# -> true
# search("b..") -> true
# param_2 = obj.search(word)
