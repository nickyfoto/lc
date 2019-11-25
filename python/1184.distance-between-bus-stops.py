#
# @lc app=leetcode id=1184 lang=python3
#
# [1184] Distance Between Bus Stops
#
# https://leetcode.com/problems/distance-between-bus-stops/description/
#
# algorithms
# Easy (56.82%)
# Total Accepted:    7.2K
# Total Submissions: 12.6K
# Testcase Example:  '[1,2,3,4]\n0\n1'
#
# A bus has n stops numbered from 0 to n - 1 that form a circle. We know the
# distance between all pairs of neighboring stops where distance[i] is the
# distance between the stops number i and (i + 1) % n.
# 
# The bus goes along both directions i.e. clockwise and counterclockwise.
# 
# Return the shortest distance between the given start and destination
# stops.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: distance = [1,2,3,4], start = 0, destination = 1
# Output: 1
# Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: distance = [1,2,3,4], start = 0, destination = 2
# Output: 3
# Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: distance = [1,2,3,4], start = 0, destination = 3
# Output: 4
# Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# distance.length == n
# 0 <= start, destination < n
# 0 <= distance[i] <= 10^4
# 
#
class Solution:
    # def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    def distanceBetweenBusStops2(self, distance, start: int, destination: int) -> int:

        n = len(distance)
        # cw # clockwise
        # ccw # counterclockwise

        # def cw(start, destination):
        #     d = 0
        #     while start != destination:
        #         d += distance[start]
        #         start += 1
        #     return d


        # def ccw(start, destination):
        #     d = 0
        #     while start != destination:
        #         d += distance[(start-1)%n]
        #         start = (start - 1) % n

        #     return d


        # print(cw(0, 1))
        # print(cw(0, 2))
        # print(cw(0, 3))
        # print(cw(1, 3))

        # print(ccw(0, 1))
        # print(ccw(0, 2))
        # print(ccw(0, 3))
        # print(ccw(3, 1))


        right, left = start, start
        cwd, ccwd = 0, 0
        while right != destination and left != destination:

            if cwd >= ccwd:
                ccwd += distance[(left-1)%n]
                left = (left-1) % n
            else:
                cwd += distance[right]
                right = (right + 1) % n
                



        # print(right, left)
        if right == destination:
            return cwd
        else:
            return ccwd




    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        n = len(distance)
        def cw(start, destination):
        # cw distance
            if destination >= start:
                return sum(distance[start:destination])
            else:
                # print(n)
                return sum(distance[start:n] + distance[:destination])



        # def ccw(start, destination):
        #     if destination >= start:
        #         # return sum(distance[destination:n] + distance[:start])
        #         return cw(destination, start)
        #     else:
        #         return sum(distance[destination:start])
        res = cw(start, destination)
        return min(res, sum(distance) - res)

# s = Solution()
# distance = [1,2,3,4]
# start = 0
# destination = 1
# print(s.distanceBetweenBusStops(distance, start, destination))



# distance = [1,2,3,4]
# start = 0
# destination = 2
# print(s.distanceBetweenBusStops(distance, start, destination))



# distance = [1,2,3,4]
# start = 0
# destination = 3
# print(s.distanceBetweenBusStops(distance, start, destination))








# distance = [7,10,1,12,11,14,5,0]
# start = 7
# destination = 2
# print(s.distanceBetweenBusStops(distance, start, destination)) #17
















