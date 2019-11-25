#
# @lc app=leetcode id=781 lang=python3

from collections import Counter
import math
class Solution:
    # def numRabbits(self, answers: List[int]) -> int:
    def numRabbits(self, answers):
        if not answers:
            return 0



        # n = len(answers)
        c = Counter(answers)
        # print(c)
        # len(c) #minimum number of colors
        # if v == 1, then that color have v+1 rabbit
        # if v > 1: then k+1
        res = 0
        for k,v in c.items():
            quo, r = divmod(v, k+1)
            if r:
                # print('here', v)
                res += v + k-(r-1)
            else:
                res += v
        # print(res)
        return res


s = Solution()
answers = [1, 1, 2]
print(s.numRabbits(answers) == 5)
answers = [10, 10, 10]
print(s.numRabbits(answers) == 11)



answers = [1,0,1,0,0]
print(s.numRabbits(answers) == 5)

answers = [0,0,1,1,1]
print(s.numRabbits(answers) == 6)


answers = [3,3]
print(s.numRabbits(answers) == 4)
answers = [3,3,3]
print(s.numRabbits(answers) == 4)
answers = [3,3,3,3]
print(s.numRabbits(answers) == 4)
answers = [3,3,3,3,3]
print(s.numRabbits(answers) == 8)




answers = [2,2,0,0,2]
print(s.numRabbits(answers) == 5)

answers = [1,1,1]
print(s.numRabbits(answers) == 4)

answers = [2,2,2,2,2,2,2]
print(s.numRabbits(answers) == 9)


answers = [2,1,2,2,2,2,2,2,1,1]
print(s.numRabbits(answers) == 13)

answers = [0,0,0]
print(s.numRabbits(answers) == 3)

answers = [1]
print(s.numRabbits(answers) == 2)


answers = [0,0,0,1]
print(s.numRabbits(answers) == 5)

answers = [2,2,2]
print(s.numRabbits(answers) == 3)

answers = [4]*6
# print(s.numRabbits(answers))
print(s.numRabbits(answers) == 10)


answers = [3]*7
print(s.numRabbits(answers) == 8)

answers = [0,3,2,0,3,3,4,2,4,3,2,4,4,3,0,1,3,4,4,3]
print(s.numRabbits(answers) == 26)
        
