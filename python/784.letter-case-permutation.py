#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (56.11%)
# Total Accepted:    45.5K
# Total Submissions: 80.4K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#
class Solution:
    # def letterCasePermutation(self, S: str) -> List[str]:
    def letterCasePermutation(self, S):
        n = len(S)
        num_of_letters = len([l for l in S if l not in "0123456789"])
        # print(num_of_letters)
        if num_of_letters == 0:
            return [S]
        letter_indices = [i for i in range(n) if S[i] not in "0123456789"]
        # print(letter_indices)
        res = []
        S = list(S)
        for i in range(2**num_of_letters):
            p = list(bin(i)[2:])
            while len(p) < num_of_letters:
                p.insert(0, '0')
            # print(p)
            for j in range(len(p)):
                if p[j] == '0':
                    S[letter_indices[j]] = S[letter_indices[j]].lower()
                else:
                    S[letter_indices[j]] = S[letter_indices[j]].upper()
            res.append("".join(S))
        return res



# s = Solution()
# S = "a1b2"
# print(s.letterCasePermutation(S))


# S = "3z4"
# print(s.letterCasePermutation(S))


# S = "12345"
# print(s.letterCasePermutation(S))


# S = "mQe"
# print(s.letterCasePermutation(S))

