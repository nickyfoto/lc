#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#
# https://leetcode.com/problems/binary-watch/description/
#
# algorithms
# Easy (45.37%)
# Total Accepted:    64.5K
# Total Submissions: 142.2K
# Testcase Example:  '0'
#
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the
# right.
# 
# For example, the above binary watch reads "3:25".
# 
# Given a non-negative integer n which represents the number of LEDs that are
# currently on, return all possible times the watch could represent.
# 
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04",
# "0:08", "0:16", "0:32"]
# 
# 
# Note:
# 
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid,
# it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for
# example "10:2" is not valid, it should be "10:02".
# 
# 
#

class Solution:
    # def readBinaryWatch(self, num: int) -> List[str]:
    def readBinaryWatch(self, num):
        if num == 0:
            return ["0:00"]
        # from itertools import permutations
        # l = [0, 0, 1]
        # print(l)
        # print(list(permutations(l,2)))



        class unique_element:
            def __init__(self,value,occurrences):
                self.value = value
                self.occurrences = occurrences

        def perm_unique(elements):
            eset=set(elements)
            listunique = [unique_element(i,elements.count(i)) for i in eset]
            u=len(elements)
            return perm_unique_helper(listunique,[0]*u,u-1)

        def perm_unique_helper(listunique,result_list,d):
            if d < 0:
                yield tuple(result_list)
            else:
                for i in listunique:
                    if i.occurrences > 0:
                        result_list[d]=i.value
                        i.occurrences-=1
                        for g in  perm_unique_helper(listunique,result_list,d-1):
                            yield g
                        i.occurrences+=1




        a = list(perm_unique([0] * (10-num) + [1] * num))
        # print(a)
        # print(len(a))


        def func(l):
            hour = l[:4]
            minutes = l[4:]

            hour = int("".join([str(s) for s in hour]), 2)
            # print(hour)
            minutes = int("".join([str(s) for s in minutes]), 2)
            # print(minutes)
            if minutes < 10:
                minutes = '0' + str(minutes)
            if hour < 12 and int(minutes) < 60:
                return str(hour)+":"+str(minutes)

        # print(list(map(func, a)))
        return sorted(list(filter(lambda x: x != None, map(func, a))))
        
# s = Solution()
# num = 2
# print(s.readBinaryWatch(num))

# a = [1,2,3]
# def f(x):
#     if x > 1:
#         return x*x
# print(list(filter(lambda x: x != None, map(f, a))))


# my = ['0:03','0:05','0:06','0:09','0:10','0:12','0:17','0:18','0:20','0:24','0:33','0:34','0:36', '0:40', '0:48', '10:00', '1:01', '1:02', '1:04', '1:08', '1:16', '1:32', '2:01', '2:02', '2:04', '2:08', '2:16', '2:32', '3:00', '4:01', '4:02', '4:04', '4:08', '4:16', '4:32', '5:00', '6:00', '8:01', '8:02', '8:04', '8:08', '8:16', '8:32', '9:00']
# ex = ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
     # ['0:03','0:05','0:06','0:09','0:10','0:12','0:17','0:18','0:20','0:24','0:33','0:34','0:36','0:40','0:48','10:00', '12:00', '1:01', '1:02', '1:04', '1:08', '1:16', '1:32', '2:01', '2:02', '2:04', '2:08', '2:16', '2:32', '3:00', '4:01', '4:02', '4:04', '4:08', '4:16', '4:32', '5:00', '6:00', '8:01', '8:02', '8:04', '8:08', '8:16', '8:32', '9:00']
# print(sorted(my))






















        
