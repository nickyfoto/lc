#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (49.86%)
# Total Accepted:    411.5K
# Total Submissions: 825.3K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#
from collections import defaultdict, Counter
class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        n = len(strs)
        ints = list(map(lambda x: tuple(sorted(map(ord, list(x)))), strs))
        # print(ints)
            
        arr = sorted(zip(ints, strs))
        # print(arr)
        res = []
        i = 0
        while i < n:
            template = arr[i][0]
            l = [arr[i][1]]
            j = i+1
            while j < n and arr[j][0] == template:
                l.append(arr[j][1])
                j += 1
            res.append(l)
            i = j
        # for r in res:
            # print(r)
        return res




# s = Solution()
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(s.groupAnagrams(strs))






# strs = ["ray","cod","abe","ned","arc","jar","owl","pop","paw","sky","yup","fed","jul","woo","ado","why","ben","mys","den","dem","fat","you","eon","sui","oct","asp","ago","lea","sow","hus","fee","yup","eve","red","flo","ids","tic","pup","hag","ito","zoo"]
# expected = [["hag"],["pup"],["ids"],["ito"],["flo"],["red"],["hus"],["sow"],["asp"],["oct"],["sui"],["fee"],["eon"],["tic"],["sky"],["ago"],["paw"],["jul"],["pop"],["jar"],["den","ned"],["owl"],["eve"],["mys"],["abe"],["zoo"],["ado"],["ray"],["cod"],["lea"],["arc"],["dem"],["fat"],["yup","yup"],["woo"],["fed"],["why"],["ben"],["you"]]
# res = s.groupAnagrams(strs)
# print(res)
# print(len(expected), list(map(len, expected)))
# print(len(res), list(map(len, res)))
# print(sorted(list(map(set, expected))), len(expected))





















