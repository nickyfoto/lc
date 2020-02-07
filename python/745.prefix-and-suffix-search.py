#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (32.86%)
# Likes:    266
# Dislikes: 180
# Total Accepted:    16K
# Total Submissions: 48.7K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]],["a","e"]]'
#
# Given many words, words[i] has weight i.
# 
# Design a class WordFilter that supports one function, WordFilter.f(String
# prefix, String suffix). It will return the word with given prefix and suffix
# with maximum weight. If no word exists, return -1.
# 
# Examples:
# 
# 
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
# 
# 
# 
# 
# Note:
# 
# 
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.
# 
# 
# 
# 
#

# @lc code=start
# from lcpy import Trie

class Node:
    def __init__(self, c):
        self.c = c
        self.left = None
        self.right = None
        self.mid = None
        self.val = None

class Trie:
    """
    Ternary search tries.
    """
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

    def insert(self, word, val = 1) -> None:
        """
        Inserts a word into the trie.
        """
        key = word
        # val = 1
        self.root = self.put(self.root, key, val, d=0)

    def _get(self, node, key, d):
        if not node:
            return None
        c = key[d]
        if c < node.c:
            return self._get(node.left, key, d)
        elif c > node.c:
            return self._get(node.right, key, d)
        elif d < len(key) - 1:
            return self._get(node.mid, key, d+1)
        else:
            return node

    def get(self, key):
        node = self._get(self.root, key, 0)
        if node:
            return node.val
        return None

    def contains(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        key = word
        node = self._get(self.root, key, 0)
        if not node:
            return False
        # print(node.val)
        if not node.val:
            return False
        else:
            return True

    def keys(self):
        """
        return list of string keys
        """
        result = []
        self.collect(self.root, "", result)
        return result

    def collect(self, node, prefix, result):
        if not node:
            return
        self.collect(node.left, prefix, result)
        if node.val != None:
            result.append(prefix + node.c)
        self.collect(node.mid, prefix + node.c, result)
        # prefix = prefix[:-1]
        self.collect(node.right, prefix, result)

    def startsWith(self, prefix: str) -> [str]:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        if prefix is "", return all keys
        """
        if not prefix:
            return self.keys()        
        result = []
        node = self._get(self.root, prefix, 0)
        if not node:
            return result
        if node.val != None:
            result.append(prefix)
        self.collect(node.mid, prefix, result)
        return result

class WordFilter:

    # def __init__(self, words: List[str]):
    def __init__(self, words):
        self.t = Trie()
        for i, word in enumerate(words):
            self.t.insert(word, i)

    # def f(self, prefix: str, suffix: str) -> int:
    def f(self, prefix, suffix):
        keys = self.t.startsWith(prefix)
        if suffix:
            weights = [self.t.get(k) for k in keys if k[-len(suffix):] == suffix]
        else:
            weights = [self.t.get(k) for k in keys]
        # print('weights=', weights)
        if weights:
            return max(weights)
        return -1


# Your WordFilter object will be instantiated and called as such:
# words = ["apple"]
# obj = WordFilter(words)
# prefix, suffix = "a", "e"
# print(obj.f(prefix,suffix) == 0)
# prefix, suffix = "b", ""
# print(obj.f(prefix,suffix) == -1)
# @lc code=end
# words = ['pop']
# obj = WordFilter(words)
# prefix, suffix = ["",""]
# print(obj.f(prefix,suffix))
# print(obj.f(prefix,suffix) == 0)

# words = ["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]
# words = ['abbba', 'abbbb']
# words = [words[i] for i in [0,3]]
# words = ["abbbbbbbba"]
# obj = WordFilter(words)
# prefix, suffix = ["","abaa"]
# print(obj.f(prefix,suffix))
#   ✘ Testcase: ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
# ' +
#   '[[["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]],["","abaa"],["babbab",""],["ab","baaa"],["baaabba","b"],["abab","abbaabaa"],["","aa"],["","bba"],["","baaaaabbbb"],["ba","aabbbb"],["baaa","aabbabbb"]]


# WordFilter()
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1