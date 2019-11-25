#
# @lc app=leetcode id=835 lang=python3
from collections import Counter
class Solution:
    # def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
    def largestOverlap(self, A, B):


        n = len(B)


        if n == 1:
            return A[0][0] & B[0][0]

        da = {(r,c): 1 for r in range(n) for c in range(n) if A[r][c]}
        db = {(r,c): 1 for r in range(n) for c in range(n) if B[r][c]}


        def valid(k):
            r, c = k
            return r < n and c < n


        def translate(da, db):
            mx = 0
            for i in range(n):
                for j in range(n):
                    dbc = {(k[0]+i, k[1]+j):v for k,v in db.copy().items() if k[0]+i < n and k[1]+j < n}
                    # print(db, i, j)
                    mx = max(mx, len([k for k in dbc if k in da]))
            return mx
        # print(translate(da, db))
        # print(translate(db, da))
        return max(translate(da, db), translate(db, da))

        # print(da)
        # print(db)


    def largestOverlap(self, A, B):
        N = len(A)
        LA = [i // N * 100 + i % N for i in range(N * N) if A[i // N][i % N]]
        LB = [i // N * 100 + i % N for i in range(N * N) if B[i // N][i % N]]
        print(LA)
        print(LB)
        c = Counter(i - j for i in LA for j in LB)
        print(c)
        return max(c.values() or [0])

s = Solution()
A = [[1,1,0],
     [0,1,0],
     [0,1,0]]
B = [[0,0,0],
     [0,1,1],
     [0,0,1]]
print(s.largestOverlap(A, B) ==3)


# # A = [[1]]
# # B = [[1]]
# # print(s.largestOverlap(A, B))

# A = [[1,0],[0,0]]
# B = [[0,1],[1,0]]
# print(s.largestOverlap(A, B) == 1) # 1


