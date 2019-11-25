#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (39.21%)
# Total Accepted:    17.7K
# Total Submissions: 45K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n[[10],[],[],[],[],[4],[]]'
#
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ...,
# N-1.
# 
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person.  If there are multiple such seats, they sit
# in the seat with the lowest number.  (Also, if no one is in the room, then
# the student sits at seat number 0.)
# 
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
# returning an int representing what seat the student sat in, and
# ExamRoom.leave(int p) representing that the student in seat number p now
# leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a
# student sitting in seat p.
# 
# 
# 
# Example 1:
# 
# 
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
# [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# 
# 
# ​​​​​​​
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
# all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
# in seat number p.
# 
# 
#
# from collections import 
class ExamRoom2:

    def __init__(self, N: int):
        self.n = N
        self.arr = list(range(N))
        self.d = dict(zip(self.arr, [0]*N))
        # print(self.d)
        self.num_of_people = 0

    def getLeft(self, i):
        if i == 0:
            return float('inf')
        j = i - 1
        # print('i=', i)
        while not self.d[j]:
            if j == 0:
                return float('inf')
            j -= 1
        # print('final j=', j)
        
        return i - j

    def getRight(self, i):
        if i == self.n - 1:
            return float('inf')
        j = i + 1
        while not self.d[j]:
            # print('j=', j, self.n - 1)
            if j == self.n - 1:
                return float('inf')
            j += 1

        return j - i

    def seat(self) -> int:
        if not self.num_of_people:
            self.d[0] = 1
            self.num_of_people = 1
            return 0
        else:
            distance = [0] * self.n
            for i in range(self.n):
                if not self.d[i]:
                    left = self.getLeft(i)
                    right = self.getRight(i)
                    # print('i=', i, left, right)
                    distance[i] = min(left, right)
            # print(distance)
            pos = distance.index(max(distance))
            # print(pos)
            self.d[pos] = 1
            self.num_of_people += 1
            return pos

    def leave(self, p: int) -> None:
        self.d[p] = 0
        self.num_of_people -= 1

import bisect
class ExamRoom:

    def __init__(self, N):
        self.N = N
        self.L = []
    
    def check_right(self, i, keys):
        right = keys[i+1:]
        if not right:
            return self.n - 1 - keys[i], self.n - 1
        # dist = right[0] - k
        pos = (right[0] - keys[i]) // 2
        dist = pos - keys[i]
        # print('here', dist, pos)
        return dist, pos

    def check_left(self, i, keys):
        left = keys[:i]
        if not left:
            return keys[i], 0
        # pos = (keys[i] - left[-1]) // 2
        # dist = keys[i] - pos
        pos = left[-1] + (keys[i] - left[-1]) // 2
        dist = (keys[i] - left[-1]) // 2
        # print('i=', i, 'pos=', pos)
        # print('dist=', )
        # print(pos)
        return dist, pos

    def check(self, i, keys):
        if keys[i] == self.n - 1:
            return self.check_left(i, keys)
        if keys[i] == 0:
            return self.check_right(i, keys)
        if i != len(keys) - 1:
            return self.check_left(i, keys)
        else:
            dist_l, pos_l = self.check_left(i, keys)
            dist_r, pos_r = self.check_right(i, keys)
            # print(dist_l, pos_l)
            # print(dist_r, pos_r)
            if dist_r > dist_l:
                return dist_r, pos_r
            return dist_l, pos_l
        # print('i=', i, keys[i])
        # print(dist_l, pos_l)
    def seat2(self):
        if not self.d:
            self.d.append(0)
            return 0
        else:
            max_dist = 0
            max_pos = None
            for i in range(len(self.d)):
                # find a position from k's perspective
                dist, pos = self.check(i, self.d)
                # print('i=', i, dist, pos, max_dist)
                if dist > max_dist:
                    max_dist = dist
                    max_pos = pos

            # print(self.d, max_pos)
            bisect.insort_left(self.d, max_pos)
            return max_pos
                # print(dist, pos)

    def seat(self):
        N, L = self.N, self.L
        if not L: res = 0
        else:
            d, res = L[0], 0
            # print(list(zip(L, L[1:])))
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - L[-1] > d:
                res = N - 1
        bisect.insort(L, res)
        return res
    def leave(self, p):
        self.L.remove(p)



# Your ExamRoom object will be instantiated and called as such:

# obj = ExamRoom(10)
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# obj.leave(4)
# print(obj.seat())
# obj.leave(9)
# print(obj.seat())
# print(obj.d)
# print('='*20)
# obj.leave(0)
# print(obj.seat())
# obj.leave(9)
# print(obj.seat())

# obj = ExamRoom(1000)
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# obj.leave(499)
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())