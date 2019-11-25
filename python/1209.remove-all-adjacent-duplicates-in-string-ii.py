#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
#
# algorithms
# Medium (58.01%)
# Total Accepted:    7.8K
# Total Submissions: 13.5K
# Testcase Example:  '"abcd"\n2'
#
# Given a string s, a k duplicate removal consists of choosing k adjacent and
# equal letters from s and removing them causing the left and the right side of
# the deleted substring to concatenate together.
# 
# We repeatedly make k duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made.
# 
# It is guaranteed that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# 
# Example 2:
# 
# 
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# 
# Example 3:
# 
# 
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lower case English letters.
# 
# 
#
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        i = 0
        while i < n:
            c = s[i]
            ctn = 1
            j = i + 1
            while j < n and s[j] == c:
                ctn += 1
                j += 1
            if ctn % k != 0:
                if not stack:
                    stack.append((c, ctn % k))
                else:
                    if c == stack[-1][0]:
                        if ctn + stack[-1][1] == k:
                            stack.pop()
                        else:
                            p = stack.pop()
                            if (ctn + p[1]) % k:
                                stack.append((c, (ctn + p[1]) % k)) 
                    else:
                        stack.append((c, ctn % k))
            i = j
        return "".join([s[0]*s[1] for s in stack])

S = Solution()

s = "abcd"
k = 2
print(S.removeDuplicates(s, k) == 'abcd')


s = "deeedbbcccbdaa"
k = 3
print(S.removeDuplicates(s, k) == 'aa')


s = "pbbcggttciiippooaais"
k = 2
print(S.removeDuplicates(s, k) == 'ps')
























        
