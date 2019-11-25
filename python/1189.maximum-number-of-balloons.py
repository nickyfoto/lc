#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
# https://leetcode.com/problems/maximum-number-of-balloons/description/
#
# algorithms
# Easy (63.20%)
# Total Accepted:    4.8K
# Total Submissions: 7.6K
# Testcase Example:  '"nlaebolko"'
#
# Given a string text, you want to use the characters of text to form as many
# instances of the word "balloon" as possible.
# 
# You can use each character in text at most once. Return the maximum number of
# instances that can be formed.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: text = "nlaebolko"
# Output: 1
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: text = "loonbalxballpoon"
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: text = "leetcode"
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.
# 
#
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        

        balloon = Counter('balloon')
        c = Counter(text)
        n = 0
        get_balloon = True
        while get_balloon:
            for k,v in balloon.items():
                if k not in c:
                    get_balloon = False
                    break
                else:
                    if c[k] < v:
                        get_balloon = False
                        break
                    else:
                        c[k] -= v
            if get_balloon:
                n += 1
        # print(n)
        return n

# s = Solution()
# text = "nlaebolko"
# print(s.maxNumberOfBalloons(text))



# text = "loonbalxballpoon"
# print(s.maxNumberOfBalloons(text))



# text = "leetcode"
# print(s.maxNumberOfBalloons(text))















