#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (51.25%)
# Total Accepted:    80.2K
# Total Submissions: 156.4K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
# 
# Example 1:
# 
# 
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# Example 2:
# 
# 
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#


import re

class Solution:
    # def diffWaysToCompute(self, input: str) -> List[int]:
    def diffWaysToCompute2(self, input):
        # print(re.split('+|-|*|\n', input))
        nums = re.findall(r"[\w']+", input)
        ops = re.findall(r"[\D']+", input)

        def recur(nums, ops):
            
            # print(nums, ops)
            if not nums:
                return []
            n = len(nums)
            if n == 1:
                if ops:
                    return [nums[0] + ops[0]]
                else:
                    return [nums[0]]
            if len(nums) == 2:
                if len(ops) == 1:
                    return ['(' + nums[0] + ops[0] + nums[1] + ')']
                elif len(ops) == 2:
                    return ['(' + nums[0] + ops[0] + nums[1] + ')' + ops[1]]
            else:
                
                res = []
                for i in range(n):
                    for j in range(i+1, n):
                        total_nums = [nums[:i], nums[i:j], nums[j:]]
                        total_ops = [ops[:i], ops[i:j], ops[j:]]
                        s = []
                        for z in zip(total_nums, total_ops):
                            r = recur(*z)
                            # print('before s=', s, 'r=', r, 'length r=' , len(r))
                            s.extend(r)
                            # print('after s=', s)
                        res.append(s)
                           
                res = ["".join(x) for x in res]
                return res
        
        # print(recur(nums, ops))


        from itertools import product
        from functools import reduce
        def recur2(nums_ops):
            nums, ops = nums_ops
            # print(nums, ops)
            if not nums:
                return []
            n = len(nums)
            if n == 1:
                if ops:
                    return [nums[0] + ops[0]]
                else:
                    return [nums[0]]
            if len(nums) == 2:
                if len(ops) == 1:
                    return ['(' + nums[0] + ops[0] + nums[1] + ')']
                elif len(ops) == 2:
                    return ['(' + nums[0] + ops[0] + nums[1] + ')' + ops[1]]
            else:
                
                l = []
                for i in range(n):
                    for j in range(i+1, n):
                        total_nums = [nums[:i], nums[i:j], nums[j:]]
                        total_ops = [ops[:i], ops[i:j], ops[j:]]
                        # print(total_nums)
                        # print(total_ops)
                        res = list(map(recur2, zip(total_nums, total_ops)))
                        # print('res=', res)
                        res = [x for x in res if x]
                        res = list(product(*res))
                        def f(t):
                            s = "".join(t)
                            if s[-1] not in ['+', '-', '*']:
                                return '('+s+')' 
                            else:
                                # print(s)

                                return '('+s[:-1]+')' + s[-1] 
                            

                        # print('res2=', res)
                        res = list(map(f, res))
                            
                        l.extend(res)
                
                # print(nums, ops) 
                # l = ['('+x+')' for x in l if x[-1] not in ['+', '-', '*']]
                # print('l=', l)
                
                return l

        my = recur2((nums, ops))
        # print(len(my), len(set(my)))
        s = set()
        for x in my:
            s.add(eval(x))
        return list(s)


    def diffWaysToCompute(self, input):

        def recur(input):
            if input.isdigit():
                return [int(input)]
            res = []
            for i in range(len(input)):
                if input[i] in "-+*":
                    res1 = recur(input[:i])
                    res2 = recur(input[i+1:])
                    for j in res1:
                        for k in res2:
                            res.append(helper(j, k, input[i]))
            return res
        
        def helper(m, n, op):
            if op == "+":
                return m+n
            elif op == "-":
                return m-n
            else:
                return m*n
        return recur(input)



# s = Solution()
# input = "2-1"
# input = "2-1-1"
# input = "2*3-4*5"
# input = "2*3-4*5+6"
# print(s.diffWaysToCompute(input))

# mycode = 'print "hello world"'
# print(eval("(2*(3-(4*5)))"))
# exec('2-1-1')



# my = ['(2*(3-(4*5)))', '(2*((3-4)*5))', '(2*(3-4*5))', '((2*3)-(4*5))', '((2*(3-4))*5)', '(((2*3)-4)*5)', '((2*3-4)*5)', '(2*3-(4*5))', '(2*(3-4)*5)', '((2*3)-4*5)']



