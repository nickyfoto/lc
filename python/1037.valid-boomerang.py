class Solution:
    def isBoomerang(self, points):
        x1, y1 = tuple(points[0])
        x2, y2 = tuple(points[1])
        x3, y3 = tuple(points[2])
        if set([tuple(points[0]), tuple(points[1]), tuple(points[2])]) < 3:
            return False
        if x1 != x2:
            a = (y2-y1)/(x2-x1)
            b = y1 - a * x1
            # print(a, b)
            if a * x3 + b == y3:
                return False
            else:
                return True
        else:
            if x3 == x1:
                return False
            else:
                return True


s = Solution()
points = [[1,1],[2,3],[3,2]]
print(s.isBoomerang(points))