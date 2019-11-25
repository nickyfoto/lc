#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (75.35%)
# Total Accepted:    9.9K
# Total Submissions: 13.1K
# Testcase Example:  '"AAB"'
#
# You have a set of tiles, where each tile has one letter tiles[i] printed on
# it.  Return the number of possible non-empty sequences of letters you can
# make.
# 
# 
# 
# Example 1:
# 
# 
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
# 
# 
# 
# Example 2:
# 
# 
# Input: "AAABBC"
# Output: 188
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
# 
#
from collections import Counter
class Solution:
    def numTilePossibilities2(self, tiles: str) -> int:
        self.s = 0
        def perm_unique(elements, u):
            c = Counter(elements)
            return perm_unique_helper(c,[0]*u,u-1)

        def perm_unique_helper(c,result_list,pos):
            # print('start', result_list, c, pos)
            if pos < 0:
                self.s += 1
                yield tuple(result_list)
            else:
                for i in c:
                    if c[i] > 0:
                        # print('i=', i, 'pos =', pos, 'result_list =', result_list, c)
                        result_list[pos] = i
                        c[i] -= 1
                        for g in perm_unique_helper(c,result_list, pos - 1):
                            yield g
                        c[i] += 1
        n = len(tiles)
        
        # for r in perm_unique(tiles, 2):
            # print(r, 'here')
        for i in range(1, n+1):
            for t in perm_unique(tiles, i):
                t
        return self.s

    def numTilePossibilities(self, tiles):
        c = Counter(tiles)
        # print(c)
        n = len(tiles)
        def recur(length):
            # print('length=', length)
            if length == 1:
                l = []
                for letter in c:
                    self.res += 1
                    l.append({letter: 1})
                return l
            else:
                d = recur(length - 1)
                # print(d)
                # print('length=', length, d, 'c=', c)
                l = []
                for kk in c:
                    for i in d:
                    # print('i=', i)
                        if kk not in i:
                            self.res += 1
                            temp = dict(i)
                            temp[kk] = 1
                            l.append(temp)
                        else:
                            if c[kk] - i[kk] > 0:
                                temp = dict(i)
                                temp[kk] += 1
                                self.res += 1
                                l.append(temp)
                return l
        self.res = 0
        recur(n)
        return self.res
        
# print(list(perm_unique('AAB', 2)))
# print(list(perm_unique('AAB', 1)))
# print(list(perm_unique('AAB', 3)))
# s = Solution()
# tiles = 'A'
# print(s.numTilePossibilities(tiles) == 1)
# tiles = 'AA'
# print(s.numTilePossibilities(tiles) == 2)
# tiles = 'AB'
# print(s.numTilePossibilities(tiles) == 4)
# tiles = 'AAB'
# print(s.numTilePossibilities(tiles) == 8)
# tiles = 'AAA'
# print(s.numTilePossibilities(tiles) == 3)
# tiles = 'AAAB'
# print(s.numTilePossibilities(tiles))
# tiles = 'AAABBC'
# print(s.numTilePossibilities(tiles) == 188)