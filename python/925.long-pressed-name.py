#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.37%)
# Total Accepted:    17.5K
# Total Submissions: 39.3K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard.  Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
# 
# You examine the typed characters of the keyboard.  Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
# 
# 
# 
# Example 1:
# 
# 
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# 
# 
# 
# Example 2:
# 
# 
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed
# output.
# 
# 
# 
# Example 3:
# 
# 
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def isLongPressedName(self, name: str, typed: str) -> bool:
    def isLongPressedName(self, name, typed):
        n_idx = 0
        t_idx = 0

        while n_idx < len(name):
            s = name[n_idx]
            repeats = 1
            while n_idx+1 < len(name) and name[n_idx+1] == s: 
                repeats += 1
                n_idx += 1
            # print(s, repeats, n_idx, 't_idx=', t_idx)
            t_repeats = 0
            while t_idx < len(typed):
                t = typed[t_idx]
                if t != s:
                    return False
                t_repeats = 1
                while t_idx+1 < len(typed) and typed[t_idx+1] == s: 
                    t_repeats += 1
                    t_idx += 1
                # print('typed:', t, t_repeats, t_idx)
                if t_repeats >= repeats:
                    t_idx += 1
                    break
                else:
                    return False
            if t_repeats < repeats:
                return False
            # print('t_idx=', t_idx, len(typed))
            # if t_idx == len(typed) and n_idx != len(name):
                # print('here')
                # return False
            n_idx += 1

        return True


# s = Solution()
# name = "alex"
# typed = "aaleex"      
# print(s.isLongPressedName(name, typed) == True)

# name = "saeed"
# typed = "ssaaedd"
# print(s.isLongPressedName(name, typed) == False)

# name = "leelee"
# typed = "lleeelee"
# print(s.isLongPressedName(name, typed) == True)

# name = "laiden"
# typed = "laiden"
# print(s.isLongPressedName(name, typed) == True)


# name = "pyplrz"
# typed = "ppyypllr"
# print(s.isLongPressedName(name, typed) == False)
