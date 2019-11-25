#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (52.17%)
# Total Accepted:    266.5K
# Total Submissions: 510.7K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: 3
# Output: "III"
# 
# Example 2:
# 
# 
# Input: 4
# Output: "IV"
# 
# Example 3:
# 
# 
# Input: 9
# Output: "IX"
# 
# Example 4:
# 
# 
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
class Solution:
    def intToRoman(self, num: int) -> str:
        
        l_to_d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        d_to_l = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}

        def toRoman(num, key, k):
            # print('toRoman', num, key)
            if num == 0:
                return ""
            # print(d_to_l[key], num-key, key)
            if num < key:
                return recur(num, k)
            # print(d_to_l[key])
            right = toRoman(num - key, key, k)
            return d_to_l[key] + right

        def special_case(num, quo, key, k):
            special_num = key * quo + key
            if key == 1:
                return d_to_l[special_num - num] + toRoman(special_num, special_num, k)        
            else:
                right = toRoman(special_num, special_num, k)   
                if key // 2 not in d_to_l:
                    # print(special_num,num, special_num-num, key, key // 5)    
                    return d_to_l[key // 5] + right
                else:
                    # print('check', 'key=', key, num, d_to_l[key], right)
                    return d_to_l[key] + right

        def recur(num, k):
            key = next(k)
            # print('recur', num, key)
            # print(key)
            if num >= key:
                # print('here, key=', key, num)
                quo, r = divmod(num, key)
                # print(quo, r, key)
                if key == 1 or key // 2 in d_to_l:
                    if quo == 4 or quo == 9:
                        s = special_case(num, quo, key, k)
                        if r != 0:
                            right = recur(r, k)
                            return s + right
                        else:
                            return s

                elif key // 2 not in d_to_l:
                    # print(key + r + key // 5, 'here', r, num, key//5)
                    s = special_case(num, quo, key, k)
                    if key + r + key // 5 == 2 * key:
                        return s
                    elif key + r + key // 5 > 2 * key:
                        right = recur(r % (key//5), k)
                        # print('s=', s, 'right=', right, r, key//5)
                        return s + right

                res = toRoman(num, key, k)
                return res

            else:
                # print('here', 'num=', num, key)
                return recur(num, k)



        return recur(num, iter(d_to_l))



# s = Solution()
# print(s.intToRoman(3) == "III")
# print(s.intToRoman(4) == "IV")
# print(s.intToRoman(9) == "IX")
# print(s.intToRoman(58) == "LVIII")

# print(s.intToRoman(94) == 'XCIV')
# print(s.intToRoman(1994) == "MCMXCIV")
# print(s.intToRoman(40) == "XL")





# "MCMXCIV"










