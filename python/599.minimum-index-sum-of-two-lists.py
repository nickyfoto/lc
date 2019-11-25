#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (48.05%)
# Total Accepted:    59.6K
# Total Submissions: 123.6K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# 
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings. 
# 
# 
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
# 
# 
# 
# Example 1:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# 
# 
# Example 2:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
# 
# 
# 
# 
# Note:
# 
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
# 
# 
#
class Solution:
    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    def findRestaurant(self, list1, list2):
    	d1 = dict(zip(list1, [[x] for x in range(len(list1))]))
    	for i in range(len(list2)):
    		if list2[i] in d1:
    			d1[list2[i]].append(i)
    	score = min([sum(v) for k, v in d1.items() if len(v) > 1])
    	# print(d1)
    	# print(score)
    	return [k for k, v in d1.items() if len(v) > 1 and sum(v) == score]


# s = Solution()
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# print(s.findRestaurant(list1, list2))

        
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["KFC", "Shogun", "Burger King"]
# print(s.findRestaurant(list1, list2))