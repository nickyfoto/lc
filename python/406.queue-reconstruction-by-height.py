#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (60.76%)
# Total Accepted:    88.2K
# Total Submissions: 145.1K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# Note:
# The number of people is less than 1,100.
# 
# 
# Example
# 
# 
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
# 
# 
#
class Solution:
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    def reconstructQueue(self, people):
        n = len(people)
        people = sorted(people, key=lambda x:[x[1], x[0]])
        people = [[people[i], len([p for p in people[:i] if p[0] >= people[i][0]])] for i in range(n)]
        # people = 
        # print(people)
        i = 0
        while i < n:
            while people[i][1] > people[i][0][1]:
                # print('before switch', people[i], people[i-1])
                people[i-1], people[i] = people[i], people[i-1]
                # print('after switch', people[i], people[i-1])
                i -= 1
                people[i][1] -= 1
            i += 1
        # print(people)
        people = [p[0] for p in people]
        # print(people)

        return people

# s = Solution()
# people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# print(s.reconstructQueue(people))


























