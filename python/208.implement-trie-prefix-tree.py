#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (40.20%)
# Total Accepted:    200.7K
# Total Submissions: 495.8K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#

class Node:
    def __init__(self, c):
        self.c = c
        self.left = None
        self.right = None
        self.mid = None
        self.val = None

class Trie:

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

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
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

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        key = word
        node = self.get(self.root, key, 0)
        if not node:
            return False
        # print(node.val)
        if not node.val:
            return False
        else:
            return True


    def collect(self, node, prefix, result):
        if not node:
            return
        self.collect(node.left, prefix, result)
        if node.val != None:
            result.append(prefix + node.c)
        self.collect(node.mid, prefix + node.c, result)
        prefix = prefix[:-1]
        self.collect(node.right, prefix, result)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        result = []
        node = self.get(self.root, prefix, 0)
        if not node:
            return result
        if node.val != None:
            result.append(prefix)
        # print('here')
        self.collect(node.mid, prefix, result)
        if result:
            return True
        return False

        


# trie = Trie();
# # 
# trie.insert("apple");
# print(trie.search("apple"))#;   // returns true
# print(trie.search("app"))#     // returns false
# print(trie.startsWith("app"))#; // returns true
# trie.insert("app");   
# print(trie.search("app"))#;     // returns true