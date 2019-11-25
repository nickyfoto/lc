#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#
# https://leetcode.com/problems/push-dominoes/description/
#
# algorithms
# Medium (44.78%)
# Total Accepted:    13.7K
# Total Submissions: 30.5K
# Testcase Example:  '".L.R...LR..L.."'
#
# There are N dominoes in a line, and we place each domino vertically upright.
# 
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.
# 
# 
# 
# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left.
# 
# Similarly, the dominoes falling to the right push their adjacent dominoes
# standing on the right.
# 
# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.
# 
# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.
# 
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th
# domino has been pushed to the left; S[i] = 'R', if the i-th domino has been
# pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# 
# Return a string representing the final state. 
# 
# Example 1:
# 
# 
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# 
# 
# Example 2:
# 
# 
# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.
# 
# 
# Note:
# 
# 
# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'
# 
# 
#
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        d_indices = [i for i in range(n) if dominoes[i] != '.']
        # print(d_indices)
        
        if len(d_indices) == 1:
            idx = d_indices[0]
            if dominoes[idx] == 'L':
                for j in range(idx):
                    dominoes[j] = 'L'
            else:
                for j in range(idx+1, n):
                    dominoes[j] = 'R'
            return "".join(dominoes)

        for i in range(len(d_indices)-1):
            l, r = d_indices[i], d_indices[i+1]

            if i == 0:
                if dominoes[l] == 'L':
                    for j in range(l):
                        dominoes[j] = 'L'
            if i + 1 == len(d_indices) - 1:
                if dominoes[r] == 'R':
                    for j in range(r+1, n):
                        dominoes[j] = 'R'
                # print('r=', r)
            # print(d_indices[i], d_indices[i+1])
            # print(dominoes[d_indices[i]], dominoes[d_indices[i+1]])
            if r - l > 1:
                # print(l,r,dominoes[l], dominoes[r], range(l+1, r))      
                # print(dominoes[l] + dominoes[r])
                if dominoes[l] + dominoes[r] == 'LL':
                    for j in range(l+1, r):
                        dominoes[j] = 'L'
                elif dominoes[l] + dominoes[r] == 'RR':
                    for j in range(l+1, r):
                        dominoes[j] = 'R'
                elif dominoes[l] + dominoes[r] == 'RL':
                    if (r - l) % 2 == 0:
                        mid = r + (l-r) // 2
                        # print('mid=', mid)
                        for j in range(l+1, r):
                            if j < mid:
                                dominoes[j] = 'R'
                            if j > mid:
                                dominoes[j] = 'L'
                    else:
                        mid = r + (l-r) // 2
                        # print('mid=', mid)
                        for j in range(l+1, r):
                            if j <= mid:
                                dominoes[j] = 'R'
                            else:
                                dominoes[j] = 'L'

        # print("".join(dominoes))
        return "".join(dominoes)

# s = Solution()
# dominoes = ".L.R...LR..L.."
# print(s.pushDominoes(dominoes) == "LL.RR.LLRRLL..")

# dominoes = "RR.L"
# print(s.pushDominoes(dominoes) == "RR.L")


# dominoes = "R."
# print(s.pushDominoes(dominoes) == "RR")







        
