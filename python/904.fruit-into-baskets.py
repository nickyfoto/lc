#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (41.81%)
# Total Accepted:    67.6K
# Total Submissions: 161.6K
# Testcase Example:  '[1,2,1]'
#
# In a row of trees, the i-th tree produces fruit with type tree[i].
# 
# You start at any tree of your choice, then repeatedly perform the following
# steps:
# 
# 
# Add one piece of fruit from this tree to your baskets.  If you cannot,
# stop.
# Move to the next tree to the right of the current tree.  If there is no tree
# to the right, stop.
# 
# 
# Note that you do not have any choice after the initial choice of starting
# tree: you must perform step 1, then step 2, then back to step 1, then step 2,
# and so on until you stop.
# 
# You have two baskets, and each basket can carry any quantity of fruit, but
# you want each basket to only carry one type of fruit each.
# 
# What is the total amount of fruit you can collect with this procedure?
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# 
# 
# 
# Example 4:
# 
# 
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4
# fruits.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
# 
# 
#

from collections import Counter

class Solution:
    # def totalFruit(self, tree: List[int]) -> int:
    def totalFruit(self, tree) -> int:
        c = Counter(tree)
        # print(c)

        num_of_types = len(c)
        # print(num_of_types)
        if num_of_types == 1:
            return len(tree)


        L = []
        i = 0
        n = len(tree)
        while i < n:
            t = tree[i]
            cnt = 1
            j = i+1
            while j < n and tree[j] == t:
                cnt += 1
                j += 1
            L.append((t, cnt))
            i = j

        # print(L)

        n = len(L)
        i = 1
        res = []
        while i < n:
            t1 = L[i-1][0]
            t2 = L[i][0]
            ctn = L[i-1][1] + L[i][1]
            j = i+1
            while j < n and L[j][0] in [t1, t2]:
                ctn += L[j][1]
                j += 1
            res.append(((t1, t2), ctn))
            i = j
        # print(res)
        return max(r[1] for r in res)



s = Solution()

tree =[1,2,1]
print(s.totalFruit(tree) == 3)

tree = [0,1,2,2]
print(s.totalFruit(tree) == 3)

tree = [1,2,3,2,2]
print(s.totalFruit(tree) == 4)


tree = [3,3,3,1,2,1,1,2,3,3,4]
print(s.totalFruit(tree) == 5)


tree = [0]
print(s.totalFruit(tree) == 1)























