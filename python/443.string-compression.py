#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
# https://leetcode.com/problems/string-compression/description/
#
# algorithms
# Easy (37.79%)
# Total Accepted:    56.7K
# Total Submissions: 149.2K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# Given an array of characters, compress it in-place.
# 
# The length after compression must always be smaller than or equal to the
# original array.
# 
# Every element of the array should be a character (not int) of length 1.
# 
# After you are done modifying the input array in-place, return the new length
# of the array.
# 
# 
# Follow up:
# Could you solve it using only O(1) extra space?
# 
# 
# Example 1:
# 
# 
# Input:
# ["a","a","b","b","c","c","c"]
# 
# Output:
# Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# 
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by
# "c3".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# ["a"]
# 
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# 
# Explanation:
# Nothing is replaced.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# Output:
# Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# 
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb"
# is replaced by "b12".
# Notice each digit has it's own entry in the array.
# 
# 
# 
# 
# Note:
# 
# 
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.
# 
# 
#
class Solution:
    # def compress(self, chars: List[str]) -> int:
    def compress(self, chars):
        # n = len(chars)
        i = 0
        current = chars[i]
        # res = []
        while i < len(chars):
            count = 1
            while i < len(chars) - 1 and chars[i+1] == current:
                count += 1
                # i += 1
                chars.pop(i+1)
            if count > 1:
                l = list(str(count))
                while l:
                    chars.insert(i+1, l.pop(0))
                    i += 1
                # res.extend([current, str(count)])
            # else:
                # res.append(current)
            # print(current, count, 'i=', i, chars)
            if i < len(chars) - 1:
                current = chars[i+1]
            # count = 1
            i += 1
        # chars = list("".join(res))
        # print(chars)
        return len(chars)
# s = Solution()
# chars = ["a","a","b","b","c","c","c"]
# print(s.compress(chars))
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# print(s.compress(chars))
# chars = ['a']
# print(s.compress(chars))
