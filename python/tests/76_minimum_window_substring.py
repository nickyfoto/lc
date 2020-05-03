#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (33.20%)
# Likes:    3465
# Dislikes: 247
# Total Accepted:    329K
# Total Submissions: 989.9K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict
class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    def minWindow(self, s, t):
        """
        other's answer
        """
        ct = Counter(t)
        required = len(ct)
        l = 0
        r = 0
        formed = 0
        window_counts = {}
        ans = float('inf'), None, None
        while r < len(s):
            c = s[r]
            window_counts[c] = window_counts.get(c, 0) + 1
            if c in ct and window_counts[c] == ct[c]:
                formed += 1
            while l <= r and formed == required:
                c = s[l]
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                window_counts[c] -= 1
                if c in ct and window_counts[c] < ct[c]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

    def minWindow(self, s, t):
        """
        my answer
        """
        start = 0
        length = math.inf
        ct = Counter(t)
        d = defaultdict(int)
        diff = len(ct)
        res = ""
        for i, c in enumerate(s):
            if c in ct:
                if ct[c] - d[c] == 1:
                    diff -= 1
                d[c] += 1
            if diff == 0:
                j = start
                for j in range(start, i + 1):
                    if s[j] in ct:
                        if d[s[j]] == ct[s[j]]:
                            break
                        else:
                            d[s[j]] -= 1
                start = j
                if i - start < length:
                    length = i - start
                    res = s[start:i + 1]
        return res
        

# @lc code=end
