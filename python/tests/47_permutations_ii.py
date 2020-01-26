#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (43.79%)
# Likes:    1506
# Dislikes: 52
# Total Accepted:    303.7K
# Total Submissions: 693.2K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
# from lcpy import List
class Solution:
    # def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
    def permuteUnique2(self, nums):
        # https://stackoverflow.com/questions/6284396/permutations-with-unique-values
        class unique_element:
            def __init__(self,value,occurrences):
                self.value = value
                self.occurrences = occurrences

        def perm_unique(elements):
            eset = set(elements)
            listunique = [unique_element(i,elements.count(i)) for i in eset]
            u = len(elements)
            return perm_unique_helper(listunique,[0] * u, u - 1)

        def perm_unique_helper(listunique,result_list,d):
            if d < 0:
                yield tuple(result_list)
            else:
                for i in listunique:
                    if i.occurrences > 0:
                        result_list[d] = i.value
                        i.occurrences-=1
                        for g in  perm_unique_helper(listunique, result_list, d - 1):
                            yield g
                        i.occurrences += 1
        l = perm_unique(nums)
        # print(list(map(list, l)))
        return list(map(list, l))

    def permuteUnique(self, nums):
        """
        when a number has the same val with its previous
        we can use this number only if its previous is used
        """
        def dfs(nums, used, lst, res):
            # print(nums, used, lst, res)
            if len(lst) == len(nums):
                res.append(lst.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if (i > 0 and nums[i - 1] == nums[i] and not used[i - 1]):
                    continue
                used[i] = True
                lst.append(nums[i])
                dfs(nums, used, lst, res)
                # print('i=', i, 'lst=', lst, 'res=', res)
                used[i] = False
                del lst[len(lst) - 1]
        res = []
        used = [False] * len(nums)
        lst = []
        nums.sort()
        dfs(nums, used, lst, res)
        return res
# @lc code=end
