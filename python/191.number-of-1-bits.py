
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        
        while n:
            n = n & (n - 1)
            c += 1

        return c


# s = Solution()
# print(s.hammingWeight(0x0010000000))
