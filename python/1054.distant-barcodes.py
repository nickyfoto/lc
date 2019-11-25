#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (39.77%)
# Total Accepted:    7.7K
# Total Submissions: 19.4K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
# 
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
# 
# 
# 
#
from queue import PriorityQueue
from collections import Counter
class Solution:
    # def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    def rearrangeBarcodes(self, barcodes):

        c = Counter(barcodes)

        pq = PriorityQueue()

        def pq_put(k, v):
            # v -= 1
            if v != 0:
                pq.put((-v, k))

        def pq_get():
            v, k = pq.get()
            return k, -v

        for k, v in c.items():
            pq_put(k, v)
        
        # print(pq.queue)

        res = []
        temp = []
        while not pq.empty():
            k, v = pq_get()
            if not res:
                res.append(k)
                pq_put(k, v-1)
            else:
                if k  == res[-1]:
                    temp.append((k, v))
                else:
                    res.append(k)
                    pq_put(k, v-1)
                    for item in temp:
                        k, v = item
                        pq_put(k, v)
                    temp = []
            # print(res, pq.queue, 'temp=', temp)
        # print(res)
        return res

# s = Solution()
# barcodes = [1,1,1,2,2,2]
# print(s.rearrangeBarcodes(barcodes))



# barcodes = [1,1,1,1,2,2,3,3]
# print(s.rearrangeBarcodes(barcodes))
















        
