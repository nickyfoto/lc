#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (34.63%)
# Total Accepted:    76.2K
# Total Submissions: 220K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
# 
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
# 
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: 
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# Example 2:
# 
# 
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: 
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# Example 3:
# 
# 
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
# 
# 
#
import heapq
from itertools import product
class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    def kSmallestPairs2(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        if nums1[0] > nums2[0]:
            return self.kSmallestPairs(nums2, nums1, k)

        l1 = len(nums1)
        l2 = len(nums2)
        nums1 = [[nums1[i], i, {}] for i in range(l1)]
        nums2 = [[nums2[i], i, {}] for i in range(l2)]

        def pprint():
            print('i=', i, 'n2=', n2)
            print('res=', res)
            print('nums1:', nums1)
            print('nums2:', nums2)
            print('='*30)



        res = []
        i = 0
        while i < k and nums1 and nums2:
            for n2 in range(len(nums2)):
                if nums2[n2][1] not in nums1[0][2]:
                    if n2 != 0:
                        # print('here')

                        if nums1[0][0] + nums2[n2][0] <= nums1[1][0] + nums2[n2-1][0] or (1 in nums2[n2-1][2]):

                            res.append([nums1[0][0], nums2[n2][0]])
                            i += 1
                            nums1[0][2][n2] = None
                            nums2[n2][2][nums1[0][1]] = None
                            pprint()
                            if len(nums1[0][2]) == min(k, l2):
                                nums1.pop(0)
                            if len(nums2[0][2]) == min(k, l1):
                                nums2.pop(0)
                            break
                        else:
                            # print('res=', res)
                            # print('n2=', n2)
                            # todo

                            res.append([nums1[1][0], nums2[n2-1][0]])
                            i += 1
                            nums1[1][2][n2-1] = None
                            nums2[n2-1][2][1] = None
                            pprint()
                            break

                    else:
                        res.append([nums1[0][0], nums2[n2][0]])
                        i += 1
                        nums1[0][2][n2] = None
                        nums2[n2][2][nums1[0][1]] = None
                        pprint()
                        if len(nums1[0][2]) == min(k, l2):
                            nums1.pop(0)
                        if len(nums2[0][2]) == min(k, l1):
                            nums2.pop(0)
                        break


            # i += 1

        # print(res)
        return res

    def kSmallestPairs1(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []

        pq = []
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(pq, (n1+n2, [n1, n2]))
        res = []
        i = 0
        while i < k and pq:
            s, l = heapq.heappop(pq)
            # print(s, l)
            res.append(l)
            i += 1
            # res.append
        return res

    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []

        l = list(product(nums1, nums2))
        l.sort(key=lambda x: sum(x))
        # print(l[:k])
        return list(map(list, l[:k]))

s = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(s.kSmallestPairs(nums1, nums2, k) == [[1,2],[1,4],[1,6]])

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(s.kSmallestPairs(nums1, nums2, k) == [[1,1],[1,1]])




nums1 = [1,2]
nums2 = [3]
k = 3
print(s.kSmallestPairs(nums1, nums2, k) == [[1,3],[2,3]])





nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(s.kSmallestPairs(nums1, nums2, k))


#exp = [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]



















        
