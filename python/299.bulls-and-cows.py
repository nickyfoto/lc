#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Easy (40.28%)
# Total Accepted:    106.3K
# Total Submissions: 263.8K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
# 
# Please note that both secret number and friend's guess may contain duplicate
# digits.
# 
# Example 1:
# 
# 
# Input: secret = "1807", guess = "7810"
# 
# Output: "1A3B"
# 
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# 
# Example 2:
# 
# 
# Input: secret = "1123", guess = "0111"
# 
# Output: "1A1B"
# 
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
# 
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = Counter(secret)
        g = Counter(guess)
        bull = 0
        cow = 0
        n = len(guess)

        # for i, k in enumerate(s):
        #     print(i, k)
        #     if guess[i] == k:
        #         bull += 1
        #     else:
        #         if guess[i] in 
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
                s[secret[i]] -= 1
                g[secret[i]] -= 1
        # print(s)
        for i in range(n):
            if g[guess[i]] > 0:
                if guess[i] in s and s[guess[i]] > 0:
                    cow += 1
                    s[guess[i]] -= 1
                    g[guess[i]] -= 1
        # print(bull, cow) 
        return str(bull)+'A'+str(cow)+'B'

# s = Solution()
# secret = "1807"
# guess = "7810"
# print(s.getHint(secret, guess))

# secret = "1123"
# guess = "0111"
# print(s.getHint(secret, guess))


# secret = "11"
# guess = "10"
# print(s.getHint(secret, guess))