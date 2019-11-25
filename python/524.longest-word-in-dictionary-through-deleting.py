#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (46.51%)
# Total Accepted:    48.9K
# Total Submissions: 105.2K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#
class Solution:
    # def findLongestWord(self, s: str, d: List[str]) -> str:
    def findLongestWord(self, s, d):
        if not s:
            return ""
        n = len(s)
        res = []
        temp = ""
        d = sorted(d, key=len, reverse=True)
        for word in d:
            i = 0
            j = 0
            lw = len(word)
            if res:
                if lw < len(res[0]):
                    continue
            # else:
            # if res:
                # print(lw < len(res[0]), res, word, len(res[0]), lw)
            # print(res, word)
            while i < lw:
                char = word[i]
                # print(j, n)
                if s[j] == char:
                    i += 1
                    j += 1
                    if n-j<lw-i or j == n:
                        break
                else:
                    j += 1    
                    if n-j<lw-i or j == n:
                        break
            if i == lw:
                # print(word)
                
                # res.append(word)

                if not res:
                    res.append(word)
                else:
                    if lw > len(res[0]):
                        res = [word]
                        # print('here')
                    elif lw == len(res[0]):
                        res.append(word)


            # print(i)
        # print(temp)
        # print(res[0])
        # print(res)
        if res:
            return sorted(res)[0]
        else:
            return ""

# S = Solution()
# s = "abpcplea"
# d = ["ale","apple","monkey","plea"]
# d = ["ale", "apple"]
# d = ["monkey"]
# d = ["plea"]
# print(S.findLongestWord(s, d))



# s = "abpcplea"
# d = ["a","b","c"]
# print(S.findLongestWord(s, d))


# s = "abpcplea"
# d = ["a","b","c","d"]
# print(S.findLongestWord(s, d))


# s = 'a'
# d = ['a']
# print(S.findLongestWord(s, d))


# s = "abpcplea"
# d = ["ale","apple","monkey","plea"]









# d = ["ale","apple","monkey","plea"]
# print(sorted(d, key=len, reverse=True))








        
