#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (43.79%)
# Total Accepted:    40K
# Total Submissions: 91K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# 
# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter target, find the smallest element in the list that
# is larger than the given target.
# 
# Letters also wrap around.  For example, if the target is target = 'z' and
# letters = ['a', 'b'], the answer is 'a'.
# 
# 
# Examples:
# 
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# 
# 
# 
# Note:
# 
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique
# letters.
# target is a lowercase letter.
# 
# 
#
class Solution:
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    def nextGreatestLetter(self, letters, target):
        # print(target)
        if target >= letters[-1]:
            return letters[0]
        n = len(letters)
        if n == 1:
            return letters[0]
        mid = n // 2
        if letters[mid] == target:
            idx = mid+1
            while idx < n:
                if letters[idx] > target:
                    return letters[idx]
                idx += 1
            return letters[0]
        elif letters[mid] > target:
            if letters[mid-1] <= target:
                return letters[mid]
            else:
                return self.nextGreatestLetter(letters[:mid], target)
        else:
            return self.nextGreatestLetter(letters[mid:], target)


# s = Solution()

# letters = ["e","e","e","k","q","q","q","v","v","y"]
# target = "q"
# expected v
# print(s.nextGreatestLetter(letters, target))

# a = ['a', 'b']
# t = 'z'
# print(s.nextGreatestLetter(a, t) == 'a')
# letters = ["c", "f", "j"]
# target = "a"
# print(s.nextGreatestLetter(letters, target) == 'c')

# letters = ["c", "f", "j"]
# target = "c"
# print(s.nextGreatestLetter(letters, target) == 'f')


# letters = ["c", "f", "j"]
# target = "d"
# # Output: "f"
# print(s.nextGreatestLetter(letters, target) == 'f')
# # 
# # Input:
# letters = ["c", "f", "j"]
# target = "g"
# # Output: "j"
# print(s.nextGreatestLetter(letters, target) == 'j')
# # 
# # Input:
# letters = ["c", "f", "j"]
# target = "j"
# # Output: "c"
# print(s.nextGreatestLetter(letters, target) == 'c')
# # 
# # Input:
# letters = ["c", "f", "j"]
# target = "k"
# # Output: "c"
# print(s.nextGreatestLetter(letters, target) == 'c')
