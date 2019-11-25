#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (31.60%)
# Total Accepted:    47.4K
# Total Submissions: 149.4K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
# 
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
# 
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
# 
# Note:
# 
# 
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
#
# import time

class Solution:

    
    # def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    def should_cover(self, h, houses, house_idx, heater_idx, reduced_r, heaters, dist1, debug=True):
        l = len(heaters)
        ht = heaters[heater_idx]
        condition1 = (h <= ht + reduced_r) and (h >= ht - reduced_r)
                     # 1 block way from current heater's right range  # either heater_idx is the last heater # heater_idx is not the last heater but next heater is too far way
        if condition1:
            if debug:
                print("\thouse idx", house_idx, "is covered by heater", heater_idx)
                if h < ht:
                    print("\thouse is on the LEFT of heater:", h, "<", ht)
                elif h > ht:
                    print("\thouse is on the RIGHT of heater:", h, ">", ht)
                else:
                    print("\thouse is ON the heater:", h, "=", ht)
            return True


        condition3 = ht - reduced_r - h == 1

        if condition3:
            if debug:
                print("condition3")
                print('save to dist1')
                print("\thouse is one block way from heater's left reach")
            dist1.append(h)
            return True

        condition2 = (h == ht + reduced_r + 1) and \
                      ((heater_idx == l - 1) or ((heater_idx != l - 1) and \
                      (heaters[heater_idx+1] - reduced_r - 1 > h)))
        if condition2:
            if debug:
                print("condition2")
                print('save to dist1')
            dist1.append(h)
            return True
        
        

        return False


    def checkR2(self, houses, heaters, r, start_house_idx, start_heater_idx=0, debug=True):
        reduced_r = r - 1
        if debug:
            print("reduced_r=", reduced_r)
            print("start_heater_idx=", start_heater_idx)
        if start_house_idx:
            house_idx = start_house_idx
        else:
            house_idx = 0
        dist1 = []
        while house_idx < len(houses):
            if debug:
                # print("15225", houses[15225], houses[-1])
                print("start while loop")
                print("=" * 20)
            for heater_idx in range(start_heater_idx, len(heaters)):
                if houses[house_idx:]:
                    if debug:
                        print("start heater idx", heater_idx, 'value:', heaters[heater_idx])
                        print("check house  idx", house_idx, 'value:', houses[house_idx])
                    # houses[house_idx] is not covered by heater left
                    dist_to_left = heaters[heater_idx] - reduced_r - houses[house_idx]
                    dist_to_right = houses[house_idx] - (heaters[heater_idx] + reduced_r)
                    if dist_to_left > 1:
                        # at least one house not covered 
                        # and min_dist > 1 meaning r is too small
                        if heater_idx != 0:
                            previous_dist = houses[house_idx] - (heaters[heater_idx-1] + reduced_r)
                            if debug:
                                print("heater", heater_idx-1, "on the LEFT can't cover house", house_idx, ", distance=", previous_dist)
                                print("check heater on the RIGHT of current houses")
                                print("heater", heater_idx, "can't cover", house_idx)
                                print("distance=", dist_to_left)
                                print("house_idx:", house_idx, "not covered")
                                print('r is too small\n')
                            return (- min(previous_dist, dist_to_left), house_idx, heater_idx-1)
                        else:
                            if debug:
                                print("No heater on the LEFT of house")
                                print("check heater on the RIGHT of current houses")
                                print("heater", heater_idx, "can't cover", house_idx)
                                print("distance=", dist_to_left)
                                print("house_idx:", house_idx, "not covered")
                                print('r is too small\n')
                        # return - dist_to_left
                            return (- dist_to_left, house_idx, heater_idx-1)
                        # return (- dist_to_left, house_idx, heater_idx)
                    # house[house_idx] out of right most heater's range
                    elif dist_to_right > 1:
                        # last the right most heater still not cover it
                        if heater_idx == len(heaters)-1:
                                # return - dist_to_right
                                return (- dist_to_right, house_idx, heater_idx-1)
                        else:
                            if debug:
                                print("heater", heater_idx, "on the LEFT can't cover house", house_idx, ", distance=", dist_to_right)
                                print("proceed to next heater")
                            pass
                    else:
                        # if houses[house_idx] is covered by heater
                        # update house_idx
                        while house_idx < len(houses) and self.should_cover(houses[house_idx], 
                                                                            houses,
                                                                            house_idx,
                                                                            heater_idx,
                                                                            reduced_r,
                                                                            heaters,
                                                                            dist1):
                            house_idx += 1
                            if debug:
                                print("house_idx increased to", house_idx)
                    if debug:
                        print("heater", heater_idx, "can't cover", house_idx)
                        print("Done with heater", heater_idx)
                        print("=" * 20)
        if debug:        
            print("no more houses to check")        
        if dist1:
            # the correct range
            return 0, None, 0
        else:
            if debug:
                print("dist1 is empty")
                print('r is too big\n')
            return 1, None, 0




    def findRadius(self, houses, heaters):    
        houses.sort()
        heaters.sort()
        N, i, maxRadius = len(heaters), 0, 0

        for house in houses:
            while i+1 < N and heaters[i+1] < house:
                i += 1
            maxRadius = max(maxRadius, min([abs(h-house) for h in heaters[i:i+2]]))    

        return maxRadius




        
        

        
# import time

# s = Solution()
# houses = [1,2,3]
# heaters = [2]
# print(s.findRadius(houses, heaters) == 1)

# houses = [1,2,3,4]
# heaters = [1,4]
# print(s.findRadius(houses, heaters) == 1)


# houses = list(range(1, 10))
# heaters = [1,4]
# print(s.findRadius(houses, heaters) == 5)


# houses = [1,5]
# heaters = [2]
# print(s.findRadius(houses, heaters) == 3)


# houses = [1,5]
# heaters = [10]
# print(s.findRadius(houses, heaters) == 9)


# houses = [1]
# heaters = [1,2,3,4]
# # test 4/30
# print(s.findRadius(houses, heaters) ==0)

# houses = [1,2,3]
# heaters = [1,2,3]

# print(s.findRadius(houses, heaters) ==0)


# houses = [474833169,264817709,998097157,817129560]
# heaters = [197493099,404280278,893351816,505795335]
# # print(s.findRadius(houses, heaters))
# print(s.findRadius(houses, heaters) ==104745341)



# houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
# heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
# print(s.findRadius(houses, heaters) == 161834419)

# houses = [636807826,563613512,101929267,580723810,704877633,358580979,624379149,128236579]
# heaters = [530511967,110010672]
# print(s.findRadius(houses, heaters) == 174365666)



