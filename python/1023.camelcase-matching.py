#
# @lc app=leetcode id=1023 lang=python3
#
# [1023] Camelcase Matching
#
# https://leetcode.com/problems/camelcase-matching/description/
#
# algorithms
# Medium (56.22%)
# Total Accepted:    9.5K
# Total Submissions: 17K
# Testcase Example:  '["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]\n"FB"'
#
# A query word matches a given pattern if we can insert lowercase letters to
# the pattern word so that it equals the query. (We may insert each character
# at any position, and may insert 0 characters.)
# 
# Given a list of queries, and a pattern, return an answer list of booleans,
# where answer[i] is true if and only if queries[i] matches the pattern.
# 
# 
# 
# Example 1:
# 
# 
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FB"
# Output: [true,false,true,true,false]
# Explanation: 
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
# 
# Example 2:
# 
# 
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBa"
# Output: [true,false,true,false,false]
# Explanation: 
# "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
# 
# 
# Example 3:
# 
# 
# Input: queries =
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern =
# "FoBaT"
# Output: [false,true,false,false,false]
# Explanation: 
# "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" +
# "est".
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= queries.length <= 100
# 1 <= queries[i].length <= 100
# 1 <= pattern.length <= 100
# All strings consists only of lower and upper case English letters.
# 
#



class Node:
    def __init__(self, R):
        self.next = [None] * R
        self.val = None
    def __str__(self):
        return str([n.val for n in self.next if n!=None])

class TrieST(object):

    def __init__(self, R):
        self.R = R
        self.root = None

    """docstring for TrieST"""
    def _put(self, x, key, val, d):
        # print('key=', key)
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
        # print(len(key))
        # while not x.next[ord(c)]:
        #     d += 1
        #     if d == len(key):
        #         break
        #     # print('d=', d)
        #     c = key[d]
        # print(key, d, c, x.next[ord(c)])
        # s += c
        # print(s)
        # if s == p:
            # return True
        # if d == len(key):
            # return None
        if not x.next[ord(c)]:
            return None
        return self._get(x.next[ord(c)], key, d+1)
        # else:
            # print('here')
    def get(self, key):
        # print('get root', self.root)
        x = self._get(self.root, key, 0)
        if x:
            return x.val
        return None

# from re import finditer
# from collections import Counter
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.is_word = False
        # print(self.child['a'])
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.child[char]
        node.is_word = True

class Solution:
    # def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    def camelMatch2(self, queries, pattern):
        # def camel_case_split(identifier):
        #     matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
        #     return [m.group(0) for m in matches]

        # if pattern.isupper():
        #     p = list(pattern)
        # else:
        #     p = camel_case_split(pattern)
        # print(p)
        def match(word):
            p = list(pattern)
            # print(p)
            word = list(word)
            while p:
                letter_p = p.pop(0)
                letters_w = word.pop(0)
                while letters_w != letter_p:
                    if word:
                        letters_w = word.pop(0)
                    else:
                        return False
                    if letters_w.isupper() and letters_w != letter_p:
                        return False
                # print(letter_p, letters_w)
            if not word:
                return True
            else:
                # print(word)
                return "".join(word).islower()
            # print(word, p)
                # lst = [lst[i][:len(p[i])] for i in range(pn)]

                # return lst == p
            # print(p)

        # print(list(map(match, queries)))
        return list(map(match, queries))

    def camelMatch(self, queries, pattern):
        # Trie
        # st = TrieST(256)
        st = Trie()
        for q in queries:
            st.put(q)
        
        def find(node, p_i, pattern, current_word, table):
            # print(table)
            if p_i >= len(pattern):
                print('up', node.is_word)
                if node.is_word:
                    key = "".join(current_word)
                    # mark the word to be true
                    print('mark', key)
                    table[key] = True
                for k in node.child:
                    print('continue', k)
                    if k.islower():
                        find(node.child[k], p_i, pattern, current_word+[k], table)
            else:
                for k in node.child:
                    if k == pattern[p_i]:
                        print('here', k, p_i,current_word)
                        find(node.child[k], p_i+1, pattern, current_word+[k], table)
                    elif k.islower():
                        print(k, p_i, current_word)
                        find(node.child[k], p_i, pattern, current_word+[k], table)
        
        table = defaultdict(lambda: False)
        # a = defaultdict(TrieNode)
        # print(a[1])
        # print(table['a'])
        find(st.root, 0, pattern, [], table)

        return [table[q] for q in queries]

s = Solution()
queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
queries = ["FooBar", "FrameBuffer"]
pattern = "FB"
print(s.camelMatch(queries, pattern))


# pattern = "FoBa"
# print(s.camelMatch(queries, pattern))

# pattern = "FoBaT"
# print(s.camelMatch(queries, pattern))

# queries =["CompetitiveProgramming","CounterPick","ControlPanel"]
# pattern = "CooP"
# print(s.camelMatch(queries, pattern))
# # expected_answer: [false,false,true]

# queries = ["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"]
# pattern = "ksvjLiknTzqn"
# print(s.camelMatch(queries, pattern))

# expected_answer: [true,true,true,true,true,true]
# print(camel_case_split('FooBar'))
# print(camel_case_split('FB'))

# print('FoBo'.isupper())

        
