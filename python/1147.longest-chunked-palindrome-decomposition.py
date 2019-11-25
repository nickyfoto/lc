#
# @lc app=leetcode id=1147 lang=python3
#
# [1147] Longest Chunked Palindrome Decomposition
#
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (58.09%)
# Total Accepted:    5.3K
# Total Submissions: 9.2K
# Testcase Example:  '"ghiabcdefhelloadamhelloabcdefghi"'
#
# Return the largest possible k such that there exists a_1, a_2, ..., a_k such
# that:
# 
# 
# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.
# 
# 
# 
# Example 1:
# 
# 
# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on
# "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
# 
# 
# Example 2:
# 
# 
# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
# 
# 
# Example 3:
# 
# 
# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on
# "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
# 
# 
# Example 4:
# 
# 
# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".
# 
# 
# 
# Constraints:
# 
# 
# text consists only of lowercase English characters.
# 1 <= text.length <= 1000
# 
#
from collections import defaultdict
class Solution:
    def longestDecomposition2(self, text: str) -> int:
        # n = list(text)
        # left = 0
        # right = n - 1
        text = list(text)
        l = []
        r = []
        res = 0
        while text:
            while text and l != r or (not l and not r):
                # print(he)
                l.append(text.pop(0))
                if text:
                    r.insert(0, text.pop())
            if l == r:
                res += 2
            else:
                res += 1
            # print(l, r)
            l = []
            r = []
        # print(res)
        return res

    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        left = 0
        right = n - 1
        # text = list(text)
        l = defaultdict(int)
        r = defaultdict(int)
        res = 0
        while text:
            while l != r or (not l and not r):
                # print(text, left)
                l[text[left]] += 1
                if left < right:
                    r[text[right]] += 1
                left += 1
                right -= 1
                if left > right:
                    break

            # print(l, r, left, right)
            if l == r:
                res += 2
            else:
                res += 1
            if left > right:
                break
            # print('out', res)
            # print(l, r)
            l = defaultdict(int)
            r = defaultdict(int)
        # print(res)
        return res


s = Solution()
text = "ghiabcdefhelloadamhelloabcdefghi"
print(s.longestDecomposition(text) == 7)


text = "merchant"
print(s.longestDecomposition(text) == 1)

text = "antaprezatepzapreanta"
print(s.longestDecomposition(text) == 11)

text = "aaa"
print(s.longestDecomposition(text) == 3)