#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (55.73%)
# Total Accepted:    24.4K
# Total Submissions: 43.7K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to
# make two strings equal.
# 
# Example 1:
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# 
# Example 2:
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e]
# to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Note:
# 0 < s1.length, s2.length .
# All elements of each string will have an ASCII value in [97, 122]. 
# 
#
from collections import defaultdict
from pprint import pprint
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # s1 = list(s1)
        # s2 = list(s2)
        # if not set(s1).intersection(set(s2)):
        #     return sum(map(ord, s1)) + sum(map(ord, s2))

        if s1 == s2:
            return 0
        

        def lcs2(s1, s2):
            # L = [[x]*len(s2) for x in [0]*len(s1)]    
            # print(L)
            d = {}
            for i in range(len(s1)):
                for j in range(len(s2)):
                    # print(i, j)
                    if s1[i] == s2[j]:
                        if i == 0 or j == 0:
                            # L[i][j] = 1
                            d[(i,j)] = [s1[i]]
                        else:
                            # L[i][j] = 1 + L[i-1][j-1]
                            d[i,j] = [s + s1[i] for s in d[(i-1,j-1)]]
                    else:
                        if i == 0 and j == 0:
                            d[(i,j)] = [""]
                        else:
                            if i == 0:
                            # L[i][j] = L[i][j-1]
                                d[(i,j)] = d[(i,j-1)]
                            elif j == 0:
                            # L[i][j] = L[i-1][j]
                                d[(i,j)] = d[(i-1,j)]
                            else:
                                # L[i][j] = max(L[i-1][j], L[i][j-1])
                                if len(d[(i-1,j)][0]) > len(d[(i,j-1)][0]):
                                    d[(i,j)] = d[(i-1,j)]
                                elif len(d[(i-1,j)][0]) < len(d[(i,j-1)][0]):
                                    d[(i,j)] = d[(i,j-1)]
                                else:
                                    d[(i,j)] = d[(i,j-1)] + d[(i-1,j)]
            # print(d)
            mx = max([sum(map(ord, s)) for s in d[(len(s1)-1,len(s2)-1)]])
            # print(d[(len(s1)-1,len(s2)-1)], mx)
            return sum(map(ord, s1)) + sum(map(ord, s2)) - 2 * mx
            # return L[len(L)-1][len(L[0])-1]

        def lcs2(s1, s2):
            L = [[x]*len(s2) for x in [0]*len(s1)]    
            # print(L)
            # d = {}
            for i in range(len(s1)):
                for j in range(len(s2)):
                    # print(i, j)
                    if s1[i] == s2[j]:
                        if i == 0 or j == 0:
                            L[i][j] = [s1[i]]
                            # L[i][j] = s1[i]
                        else:
                            # print('here')
                            L[i][j] = [s + s1[i] for s in L[i-1][j-1]]
                            # d[i,j] = [s + s1[i] for s in d[(i-1,j-1)]]
                    else:
                        if i == 0 and j == 0:
                            L[i][j] = [""]
                            # L[i][j] = [""]
                        else:
                            if i == 0:
                                L[i][j] = L[i][j-1]
                                # d[(i,j)] = d[(i,j-1)]
                            elif j == 0:
                                L[i][j] = L[i-1][j]
                                # d[(i,j)] = d[(i-1,j)]
                            else:
                                if len(L[i-1][j][0]) > len(L[i][j-1][0]):
                                    L[i][j] = L[i-1][j]
                                elif len(L[i-1][j][0]) < len(L[i][j-1][0]):
                                    L[i][j] = L[i][j-1]
                                else:
                                    # print(L[i-1][j], L[i][j-1])
                                    L[i][j] = L[i-1][j] + L[i][j-1]

                    # if j > 1 and i > 1:
                        # L[i-2][j-2] = None
                # print('i=', i)
                # if i > 1:
                #     L[i-2] = None

            print(L)
            mx = max([sum(map(ord, s)) for s in L[len(s1)-1][len(s2)-1]])
            # print(d[(len(s1)-1,len(s2)-1)], mx)
            return sum(map(ord, s1)) + sum(map(ord, s2)) - 2 * mx
            # return L[len(L)-1][len(L[0])-1]

        def lcs2(s1, s2):
            L = [[x]*len(s2) for x in [0]*len(s1)]    
            # print(L)
            # d = {}
            for i in range(len(s1)):
                for j in range(len(s2)):
                    # print(i, j)
                    if s1[i] == s2[j]:
                        if i == 0 or j == 0:
                            # L[i][j] = [s1[i]]
                            L[i][j] = s1[i]
                        else:
                            # print('here', s1[i],  L[i-1][j-1])
                            # print(L[i-1][j-1])
                            # todo
                            # L[i][j] = [s + s1[i] for s in L[i-1][j-1]]
                            L[i][j] = L[i-1][j-1] + s1[i]
                    else:
                        if i == 0 and j == 0:
                            L[i][j] = ""
                            # L[i][j] = [""]
                        else:
                            if i == 0:
                                L[i][j] = L[i][j-1]
                                # d[(i,j)] = d[(i,j-1)]
                            elif j == 0:
                                L[i][j] = L[i-1][j]
                                # d[(i,j)] = d[(i-1,j)]
                            else:
                                # print(L,i-1,j)
                                if L[i-1][j] > L[i][j-1]:
                                    L[i][j] = L[i-1][j]
                                elif L[i-1][j] < L[i][j-1]:
                                    L[i][j] = L[i][j-1]
                                else:
                                    print('here', L[i-1][j], L[i][j-1])
                                    L[i][j] = L[i-1][j]# + L[i][j-1]

                    # if j > 1 and i > 1:
                        # L[i-2][j-2] = None
                # print('i=', i)
                # if i > 1:
                    # L[i-2] = None

            print(L)
            mx = max([sum(map(ord, s)) for s in L[len(s1)-1][len(s2)-1]])
            # print(d[(len(s1)-1,len(s2)-1)], mx)
            return sum(map(ord, s1)) + sum(map(ord, s2)) - 2 * mx
            # return L[len(L)-1][len(L[0])-1]

        
        # print(d1,d2)

        def lcs2(s1, s2):
            L = [[x]*len(s2) for x in [0]*len(s1)]

            for i in range(len(L)):
                for j in range(len(L[0])):
                    if s1[i] == s2[j]:
                        if i == 0 and j == 0:
                            pass
                        else:
                            if i == 0:
                                # if d1[s1[i]].index(i) == d2[s2[j]].index(j):
                                L[i][j] = abs(L[i][j-1] - ord(s1[i]))
                                # else:
                                    # todo
                            # elif j == 0:
                            #     # print(s1[i], L[i-1][j])
                            #     L[i][j] = L[i-1][j] - ord(s1[i])
                            else:
                                if j == 0:
                                    L[i][j] = abs(L[i-1][j] - ord(s1[i]))
                                else:
                                    L[i][j] = L[i-1][j-1]
                                # L[i][j] = L[i-1][j-1]# - ord(s1[i])
                                # else:
                                    # L[i][j] = min( L[i-1][j] + ord(s1[i]), L[i][j-1] + ord(s2[j]))
                    else:
                        if i == 0 and j == 0:
                            L[i][j] = sum(map(ord, s1[i]+s2[j]))
                        else:
                            if i == 0:
                                L[i][j] = L[i][j-1] + ord(s2[j])
                            elif j == 0:
                                # print('here')
                                L[i][j] = L[i-1][j] + ord(s1[i]) 
                            else:
                                # L[i][j] = min(L[i][j-1]+ord(s2[j]), L[i-1][j]+ord(s1[i]))
                                # print(L[i-1][j], s1[i], L[i][j-1], s2[j])
                                # print(i,j, L[i-1][j], s1[i], L[i][j-1], s2[j])
                                L[i][j] = min( L[i-1][j] + ord(s1[i]), L[i][j-1] + ord(s2[j]))
            print(L, L[len(L)-1][len(L[0])-1])
            return L[len(L)-1][len(L[0])-1]

        def edit_distance2(s1, s2):

            # match
            # mismatch
            # indel
            # i == 0 all insertion
            # j == 0 all deletion
            L = [[x]*(len(s2)+1) for x in [0]*(len(s1)+1)]

            for j in range(len(s2) + 1):
                for i in range(len(s1) + 1):
                    if i == 0 and j == 0:
                        pass
                    elif i == 0:
                        L[i][j] = j
                    elif j == 0:
                        L[i][j] = i
                    else:
                        insertion = L[i][j-1] + 1
                        deletion = L[i-1][j] +1
                        match = L[i-1][j-1]
                        mismatch = L[i-1][j-1]+1
                        if s1[i-1] == s2[j-1]:
                            L[i][j] = min(insertion, deletion, match)
                        else:
                            L[i][j] = min(insertion, deletion, mismatch)
            pprint(L)
            a = []
            b = []
            def OutputAlignment(i,j):
                if i == 0 and j == 0:
                    return
                else:
                    # deletion
                    if i > 0 and L[i][j] == L[i-1][j] + 1:
                        OutputAlignment(i-1, j)
                        a.append(s1[i-1])
                        b.append('-')
                    # insertion
                    elif j > 0 and L[i][j] == L[i][j-1] + 1:
                        OutputAlignment(i,j-1)
                        a.append('-')
                        b.append(s2[j-1])
                    else:
                        OutputAlignment(i-1,j-1)
                        # print('i=', i)
                        # print(a)
                        a.append(s1[i-1])
                        b.append(s2[j-1])
            OutputAlignment(len(s1), len(s2))

            print(a)
            print(b)

            return L[-1][-1]
        # return edit_distance(s1, s2)

        def edit_distance(s1, s2):

            # match
            # mismatch
            # indel
            # i == 0 all insertion
            # j == 0 all deletion

            costs = [[x]*(len(s2)+1) for x in [0]*(len(s1)+1)]



            for j in range(len(s2) + 1):
                for i in range(len(s1) + 1):
                    if i == 0 and j == 0:
                        pass
                    elif i == 0:
                        costs[i][j] = ord(s2[j-1]) + costs[i][j-1]
                    elif j == 0:
                        costs[i][j] = ord(s1[i-1]) + costs[i-1][j]
                    else:
                        if s1[i-1] == s2[j-1]:
                            match_cost = costs[i-1][j-1]
                            costs[i][j] = match_cost
                            # insertion_cost = costs[i][j-1] + ord(s2[j-1])
                            # deletion_cost = costs[i-1][j] + ord(s1[i-1])
                            # costs[i][j] = min(match_cost, insertion_cost, deletion_cost)
                            # print(insertion_cost, deletion_cost, match_cost, costs[i][j])
                        else:
                            # mismatch_cost = costs[i-1][j-1] + ord(s2[j-1]) + ord(s1[i-1])
                            insertion_cost = costs[i][j-1]+ ord(s2[j-1])
                            deletion_cost = costs[i-1][j] + ord(s1[i-1])    
                            # costs[i][j] = min(mismatch_cost, insertion_cost, deletion_cost)
                            costs[i][j] = min(insertion_cost, deletion_cost)
                            # print(insertion_cost, deletion_cost, mismatch_cost, costs[i][j])
            return costs[-1][-1]
            
        return edit_distance(s1, s2)

        # return edit_distance(s1, s2)
# s = Solution()

# s1 = 'editing'
# s2 = 'distance'

# s1 = "sea"
# s2 = "eat"
# print(s.minimumDeleteSum(s1, s2) == 231)



# s1 = "delete"
# s2 = "leet"

# print(s.minimumDeleteSum(s1, s2) == 403)


# s1 = 'a'
# s2 = 'a'
# print(s.minimumDeleteSum(s1, s2) == 0)


# s1 = "a"
# s2 = "b"
# print(s.minimumDeleteSum(s1, s2)==195)

# s1 = "ab"
# s2 = "cd"
# print(s.minimumDeleteSum(s1, s2)==394)


# s1 = 'ab'
# s2 = 'a'
# print(s.minimumDeleteSum(s1, s2) == 98)


# s1 = 'a'
# s2 = 'ab'
# print(s.minimumDeleteSum(s1, s2) == 98)

# s1 = "s"
# s2 = "e"
# print(s.minimumDeleteSum(s1, s2) == 216)

# s1 = "se"
# s2 = "e"
# print(s.minimumDeleteSum(s1, s2) == 115)

# s1 = 's'
# s2 = 'ea'
# print(s.minimumDeleteSum(s1, s2) == 313)



# s1 = "se"
# s2 = "ea"
# print(s.minimumDeleteSum(s1, s2) == 212)



# s1 = "sea"
# s2 = "ea"
# print(s.minimumDeleteSum(s1, s2) == 115)


# s1 = "ea"
# s2 = "sea"
# print(s.minimumDeleteSum(s1, s2) == 115)


# s1 = "sea"
# s2 = "eat"
# print(s.minimumDeleteSum(s1, s2) == 231)


# s1 = "d"
# s2 = "l"
# print(s.minimumDeleteSum(s1, s2) == 208)


# s1 = "de"
# s2 = "l"
# print(s.minimumDeleteSum(s1, s2) == 309)


# s1 = "de"
# s2 = "le"
# print(s.minimumDeleteSum(s1, s2) == 208)


# s1 = "del"
# s2 = "le"
# print(s.minimumDeleteSum(s1, s2) == 302)



# s1 = "del"
# s2 = "lee"
# print(s.minimumDeleteSum(s1, s2) == 403)



# s1 = "dele"
# s2 = "lee"
# print(s.minimumDeleteSum(s1, s2) == 302)

# s1 = "dele"
# s2 = "leet"
# print(s.minimumDeleteSum(s1, s2) == 418)

# s1 = "delet"
# s2 = "leet"
# print(s.minimumDeleteSum(s1, s2) == 302)


# s1 = "delete"
# s2 = "leet"
# print(s.minimumDeleteSum(s1, s2) == 403)


# s1 = 'ac'
# s2 = 'ccac'
# print(s.minimumDeleteSum(s1, s2) == 198)



# s1 = 'ac'
# s2 = 'ca'
# print(s.minimumDeleteSum(s1, s2) == 194)


# s1 = 'cac'
# s2 = 'ac'
# print(s.minimumDeleteSum(s1, s2) == 99)

# s1 = 'ccac'
# s2 = 'ac'
# print(s.minimumDeleteSum(s1, s2) == 198)



# s1 = "ccaccjp"
# s2 = "fwosarcwge"
# print(s.minimumDeleteSum(s1, s2) == 1399)






# s1 = 'af'
# s2 = 'faf'
# print(s.minimumDeleteSum(s1, s2) == 102)


# s1 = 'faf'
# s2 = 'af'
# print(s.minimumDeleteSum(s1, s2) == 102)


# s1 = 'f'
# s2 = 'ff'
# print(s.minimumDeleteSum(s1, s2) == 102)


# s1 = 'ff'
# s2 = 'af'
# print(s.minimumDeleteSum(s1, s2) == 199)


# s1 = 'ff'
# s2 = 'fa'
# print(s.minimumDeleteSum(s1, s2) == 199)



# s1 = 'aff'
# s2 = 'f'
# print(s.minimumDeleteSum(s1, s2) == 199)

# s1 = 'f'
# s2 = 'aff'
# print(s.minimumDeleteSum(s1, s2) == 199)

# s1 = 'fqfxo'
# s2 = 'fxo'
# print(s.minimumDeleteSum(s1, s2) == 215)




# s1 = 'sjfqkfxqoditw'
# s2 = 'fxo'
# print(s.minimumDeleteSum(s1, s2) == 1096)





# s1 = "sjfqkfxqoditw"
# s2 = "fxymelgo"
# print(s.minimumDeleteSum(s1, s2) == 1638)
# # #fxo


# s1 = "igijekdtywibepwonjbwykkqmrgmtybwhwjiqudxmnniskqjfbkpcxukrablqmwjndlhblxflgehddrvwfacarwkcpmcfqnajqfxyqwiugztocqzuikamtvmbjrypfqvzqiwooewpzcpwhdejmuahqtukistxgfafrymoaodtluaexucnndlnpeszdfsvfofdylcicrrevjggasrgdhwdgjwcchyanodmzmuqeupnpnsmdkcfszznklqjhjqaboikughrnxxggbfyjriuvdsusvmhiaszicfa"
# s2 = "ikhuivqorirphlzqgcruwirpewbjgrjtugwpnkbrdfufjsmgzzjespzdcdjcoioaqybciofdzbdieegetnogoibbwfielwungehetanktjqjrddkrnsxvdmehaeyrpzxrxkhlepdgpwhgpnaatkzbxbnopecfkxoekcdntjyrmmvppcxcgquhomcsltiqzqzmkloomvfayxhawlyqxnsbyskjtzxiyrsaobbnjpgzmetpqvscyycutdkpjpzfokvi"
# print(s.minimumDeleteSum(s1, s2) == 41731)











