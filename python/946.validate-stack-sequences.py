#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
# https://leetcode.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (58.11%)
# Total Accepted:    18.1K
# Total Submissions: 31.1K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# Given two sequences pushed and popped with distinct values, return true if
# and only if this could have been the result of a sequence of push and pop
# operations on an initially empty stack.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# Output: false
# Explanation: 1 cannot be popped before 2.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
# 
# 
# 
#
class Solution:
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    def validateStackSequences(self, pushed, popped) -> bool:

        stack = []
        while popped:
            if not stack:
                stack.append(pushed.pop(0))
            else:
                if stack[-1] != popped[0]:
                    if pushed:
                        stack.append(pushed.pop(0))
                    else:
                        return False
                else:
                    stack.pop()
                    popped.pop(0)
        
        # print(stack, pushed, popped)
        if not stack and not pushed and not popped:
            return True
        return False

# s = Solution()
# pushed = [1,2,3,4,5]
# popped = [4,5,3,2,1]
# print(s.validateStackSequences(pushed, popped))



# pushed = [1,2,3,4,5]
# popped = [4,3,5,1,2]
# print(s.validateStackSequences(pushed, popped))

























        
