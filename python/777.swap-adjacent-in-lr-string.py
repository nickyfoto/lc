#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (33.70%)
# Total Accepted:    16.9K
# Total Submissions: 50K
# Testcase Example:  '"X"\n"L"'
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string end, return True if and only if there exists a sequence
# of moves to transform one string to the other.
# 
# Example:
# 
# 
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# Note:
# 
# 
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
# 
# 
#
from collections import Counter
class Solution:
    def canTransform2(self, start: str, end: str) -> bool:
        cs = Counter(start)
        ce = Counter(end)
        # print(cs, ce)
        if cs != ce:
            return False
        n = len(start)

        def transformable(i):
            if i == n-1:
                if start[i] == end[i]:
                    return True
                else:
                    return False
            else:
                return (start[i:i+2] == 'XL' and end[i:i+2] == 'LX') or \
                       (start[i:i+2] == 'RX' and end[i:i+2] == 'XR') 

        i = 0
        while i < n:
            if start[i] == end[i]:
                i += 1
            else:
                if transformable(i):
                    i += 2
                else:
                    # print(i)
                    return False
        return True

    def canTransform(self, start: str, end: str) -> bool:
        # XL -> LX means X XXXXXXXX L
        #                L XXXXXXXX X are equal
        # RX -> XR means R XXXXRXXXXRR X
        #                X XXXXRXXXXRR R are equal
        start = list(start)
        end = list(end)
        i = 0
        n = len(start)
        while i < n:
            if start[i] == end[i]:
                i += 1
            else:
                if i < n - 1:
                    if start[i]+end[i] == 'RX':
                        rx_stack = []
                        rx_stack.append(i)
                        i += 1
                        while rx_stack:
                            if start[i]+end[i] == 'RX':
                                rx_stack.append(i)
                                i += 1
                            elif start[i]+end[i] in ['XX', 'RR']:
                                i += 1
                            elif start[i]+end[i] == 'XR':
                                j = rx_stack.pop()
                                start[i], start[j] = start[j], start[i]
                                i += 1
                            else:
                                print(start, 'i=', i)
                                print(rx_stack)
                                return False
                        
                    elif start[i]+end[i] == 'XL':
                        xl_stack = []
                        xl_stack.append(i)
                        i += 1
                        while xl_stack:
                            if start[i]+end[i] == 'XL':
                                xl_stack.append(i)
                                i += 1
                            elif start[i]+end[i] in ['XX', 'LL']:
                                i += 1
                            elif start[i]+end[i] == 'LX':
                                j = xl_stack.pop()
                                start[i], start[j] = start[j], start[i]
                                i += 1
                            else:
                                print(start, 'i=', i)
                                print(xl_stack)
                                return False
                    else:
                        # print(start[i]+end[i])
                        return start[i] == end[i]

                else:

                    return start[i] == end[i]
            
            
        return True

# s = Solution()
# start = "RXXLRXRXL"
# end =   "XRLXXRRLX"
# print(s.canTransform(start, end)) #True

# start = "XXXXXLXXXX"
# end =   "LXXXXXXXXX"
# print(s.canTransform(start, end)) #True

# start = 'RXLX'
# end =   'XRXL'
# print(s.canTransform(start, end)) # False


# start = 'RXL'
# end =   'XRX'
# print(s.canTransform(start, end)) # False

# start = 'RXXXX'
# end =   'XXXXR'
# print(s.canTransform(start, end)) # True 

# start = "XLXRRXXRXX"
# end =   "LXXXXXXRRR" 
# print(s.canTransform(start, end)) # True 


#        # 01 2 3 4
# start = "XL X R RXXRXX"
# end =   "LX X X XXXRRR" 


















