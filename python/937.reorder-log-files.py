#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Log Files
#
# https://leetcode.com/problems/reorder-log-files/description/
#
# algorithms
# Easy (57.04%)
# Total Accepted:    24.8K
# Total Submissions: 43.7K
# Testcase Example:  '["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]'
#
# You have an array of logs.  Each log is a space delimited string of words.
# 
# For each log, the first word in each log is an alphanumeric identifier.
# Then, either:
# 
# 
# Each word after the identifier will consist only of lowercase letters,
# or;
# Each word after the identifier will consist only of digits.
# 
# 
# We will call these two varieties of logs letter-logs and digit-logs.  It is
# guaranteed that each log has at least one word after its identifier.
# 
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the
# identifier used in case of ties.  The digit-logs should be put in their
# original order.
# 
# Return the final order of the logs.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4
# 7"]
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the
# identifier.
# 
# 
# 
#
class Log:
    def __init__(self, identifier, content):
        self.identifier = identifier
        self.content = content


        

class Solution:
    # def reorderLogFiles(self, logs: List[str]) -> List[str]:
    def reorderLogFiles(self, logs):
        d_logs = []
        l_logs = []
        for l in logs:
            s = l.split()
            if s[1][0] in '0123456789':
                d_logs.append(l)
            else:
                l_logs.append(l)
        # print(l_logs)
        l_logs.sort(key = lambda s: (s.split()[1:], s.split()[0]))
        # print(l_logs)
        return l_logs + d_logs
# s = Solution()
# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# print(s.reorderLogFiles(logs))
# l1 = Log("a1 9 2 3 1")
# l2 = Log("g1 act car")
# print(l1 > l2)
# print(l2 > l1)
# logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
# print(s.reorderLogFiles(logs))




























        
