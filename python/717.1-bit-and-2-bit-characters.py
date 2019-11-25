#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#
# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (49.19%)
# Total Accepted:    42.9K
# Total Submissions: 87.1K
# Testcase Example:  '[1,0,0]'
#
# We have two special characters. The first character can be represented by one
# bit 0. The second character can be represented by two bits (10 or 11).  
# 
# Now given a string represented by several bits. Return whether the last
# character must be a one-bit character or not. The given string will always
# end with a zero.
# 
# Example 1:
# 
# Input: 
# bits = [1, 0, 0]
# Output: True
# Explanation: 
# The only way to decode it is two-bit character and one-bit character. So the
# last character is one-bit character.
# 
# 
# 
# Example 2:
# 
# Input: 
# bits = [1, 1, 1, 0]
# Output: False
# Explanation: 
# The only way to decode it is two-bit character and two-bit character. So the
# last character is NOT one-bit character.
# 
# 
# 
# Note:
# 1 .
# bits[i] is always 0 or 1.
# 
#
# import re
class Solution:
    # def isOneBitCharacter(self, bits: List[int]):
    # When reading from the i-th position, 
    # if bits[i] == 0,
    #   the next character must have 1 bit;
    # else if bits[i] == 1, 
    #   the next character must have 2 bits. 
    # We increment our read-pointer i to the start of the next character appropriately. 
    # At the end, if our pointer is at bits.length - 1, then the last character must have a size of 1 bit.
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
            # i += bits[i] + 1
        return i == len(bits) - 1
            # print('here')
# s = Solution()
# bits = [1, 0, 0]
# bits = [1, 1, 1, 0, 4, 0]
# print(s.isOneBitCharacter(bits))





























        
