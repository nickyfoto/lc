class MaxPQ:
    """docstring for MaxPQ"""
    def __init__(self):
        self.pq = [0]
        self.length = 0

    def swim(self, k):
        # print("self.pq=", self.pq)
        # print('k=', k)
        while k > 1 and self.pq[k//2] < self.pq[k]:
            self.pq[k//2], self.pq[k] = self.pq[k], self.pq[k//2]
            k = k // 2
        # print("after swim self.pq=", self.pq)

    def sink(self, k):
        while 2 * k <= self.length:
            j = 2 * k
            if j < self.length and self.pq[j] < self.pq[j+1]:
                j += 1
            if self.pq[k] >= self.pq[j]:
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j

    def delMax(self):
        m = self.pq[1]
        self.pq[-1], self.pq[1] = self.pq[1], self.pq[-1]
        self.pq = self.pq[:-1]
        self.length -= 1
        self.sink(1)
        return m

    def add(self, num):
        self.pq.append(num)
        self.length += 1
        self.swim(self.length)
        # print(self.pq)

    def getLength(self):
        return self.length

    def __str__(self):
        return str(self.pq)

class Solution:

    # def lastStoneWeight(self, stones: List[int]) -> int:
    def lastStoneWeight(self, stones):
        # parent of node at k is at k/2
        # children of node at k are at 2k and 2k+1
        pq = MaxPQ()
        for s in stones:
            pq.add(s)
        print('starting pq=', pq)
        while pq.getLength() > 1:
            y = pq.delMax()
            x = pq.delMax()
            print('x=', x, 'y=', y)
            if x != y:
                pq.add(y-x)
            print('pq=', pq)
        if pq.getLength() == 1:
            return pq.delMax()
        else:
            return 0

s = Solution()
stones = [2,7,4,1,8,1]
print(s.lastStoneWeight(stones))


