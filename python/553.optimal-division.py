#
# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#
# https://leetcode.com/problems/optimal-division/description/
#
# algorithms
# Medium (55.61%)
# Total Accepted:    21.6K
# Total Submissions: 38.9K
# Testcase Example:  '[1000,100,10,2]'
#
# Given a list of positive integers, the adjacent integers will perform the
# float division. For example, [2,3,4] -> 2 / 3 / 4.
# 
# However, you can add any number of parenthesis at any position to change the
# priority of operations. You should find out how to add parenthesis to get the
# maximum result, and return the corresponding expression in string format.
# Your expression should NOT contain redundant parenthesis.
# 
# Example:
# 
# Input: [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since
# they don't influence the operation priority. So you should return
# "1000/(100/10/2)". 
# 
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
# 
# 
# 
# Note:
# 
# The length of the input array is [1, 10].
# Elements in the given array will be in range [2, 1000].
# There is only one optimal division for each test case.
# 
# 
#
class Solution:
    # def optimalDivision(self, nums: List[int]) -> str:
    def optimalDivision2(self, nums):


        s = map(str, nums)
        # print("/".join(s))



        def recur(nums, maximize):
            # num comes in str
            if len(nums) > 1:
                if maximize:
                    print('maximize', nums)
                else:
                    print('minimize', nums)
            if not nums:
                return ""
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                if maximize:
                    return "/".join(nums)
                return '(' + "/".join(nums) + ')'
                

            else:
                head, tail = nums[:1], nums[1:]
                # print(head, tail)
                if not maximize:
                    return '(' + recur(head, maximize=False) + '/' + recur(tail, maximize=True) + ')'
                return recur(head, maximize=False) + '/' + recur(tail, maximize=False)


        return recur(list(s), maximize=True)


    def optimalDivision(self, nums):


        def add_parenthesis(s):
            return '(' + s + ')'

        s = map(str, nums)
        def recur(nums, maximize):
            # num comes in str
            # if len(nums) > 1:
            #     if maximize:
            #         print('maximize', nums)
            #     else:
            #         print('minimize', nums)
            if not nums:
                return ""
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return "/".join(nums)
            else:
                head, tail = nums[:1], nums[1:]
                if not maximize:
                    return recur(head, maximize=False) + '/' + recur(tail, maximize=False)
                else:
                    return recur(head, maximize=False) + '/' + add_parenthesis(recur(tail, maximize=False))
        return recur(list(s), maximize=True)



# s = Solution()

# nums = [10,2]
# print(s.optimalDivision(nums) == "10/2")

# nums = [100,10,2]
# print(s.optimalDivision(nums) == "100/(10/2)")

# nums = [2,3,4]
# print(s.optimalDivision(nums) =="2/(3/4)")

# nums = [1000,100,10,2]
# # print(s.optimalDivision(nums))
# print(s.optimalDivision(nums) == "1000/(100/10/2)")



# nums = [6,2,3,4,5]
# # print(s.optimalDivision(nums))
# print(s.optimalDivision(nums) == "6/(2/3/4/5)")




# nums = [5,1000,100,10,2]
# print(s.optimalDivision(nums))


















