


class Solution:
    def findSolution2(self, f, z):


        def cal_low_high(lo, hi):
            res = lo + (hi-lo) // 2
            if res == lo:
                exhausted = True
            else:
                exhausted = False
            return res, exhausted

        exhausted = False
        res = []
        lx, hx, ly, hy = 1, 1000, 1, 1000
        # self.upperbound = [hx, hy]
        # self.lowerbound = [lx, ly]


        def search(lx, hx, ly, hy):


            original_hy = hy
            original_ly = ly
            x, exhaust_x = cal_low_high(lx, hx)
            y, exhaust_y = cal_low_high(ly, hy)
            while not exhausted:
                # print(x, y, self.upperbound, self.lowerbound)
                # print(x, y)
                r = f(x, y)
                if r == z:
                    return x, y
                if exhaust_x and exhaust_y:
                    return None, None
                else:

                    if r > z:
                        if x == 1 and y == 1:
                            # print('here')
                            return None, None
                        # self.upperbound = update_upper(self.upperbound, x, y)
                        if not exhaust_y:
                            hy = y
                            # print('ly=', ly, 'hy=', hy)
                            y, exhaust_y = cal_low_high(ly, hy)
                            # print(x, y, exhaust_x, exhaust_y)
                        else:
                            # print('exhaust y')
                            hx = x
                            hy = original_hy
                            ly = original_ly
                            x, exhaust_x = cal_low_high(lx, hx)
                            y, exhaust_y = cal_low_high(ly, hy)
                    else:
                        if x == 1000 and y == 1000:
                            return None, None
                        # self.lowerbound = update_lower(self.lowerbound, x, y)
                        if not exhaust_y:
                            ly = y
                            y, exhaust_y = cal_low_high(ly, hy)
                        else:
                            # print('exhaust y')
                            lx = x
                            x, exhaust_x = cal_low_high(lx, hx)
                            hy = original_hy
                            ly = original_ly
                            y, exhaust_y = cal_low_high(ly, hy)
                            # print(x, y, exhaust_x, exhaust_y, ly)
        x, y = search(1, 1000, 1, 1000)
        if x is None and y is None:
            return []
        # print(x, y, 'here')
        if [x, y] not in res:
            res.append([x, y])
            print(res)
            if x > 1:
                for i in range(1, 2*x-1, 2):
                    # print('i=', i)
                    x, y = search(1, i, 1, 1000)
                    if x is None and y is None:
                        continue
                    if [x, y] not in res:
                        res.append([x, y])
            # print(x, y)
            if y and y > 1:
                for j in range(1, 2*y-1, 2):
                    print('j=', j)
                    x, y = search(1, 1000, 1, j)
                    if x is None and y is None:
                        continue
                    if [x, y] not in res:
                        res.append([x, y])
                        print(res, [x,y])
                    # else:
                        # print('here', x, y)

        return res




    def findSolution(self, f, z):

        def cal_low_high(lo, hi):
            res = lo + (hi-lo) // 2
            if res == lo:
                exhausted = True
            else:
                exhausted = False
            return res, exhausted

        res = []
        ly, hy = 1, 1000
        for i in range(1, 1001):
            y, exhaust_y = cal_low_high(ly, hy)

            while not exhaust_y:
                r = f(i, y)
                if r == z:
                    res.append([i, y])
                    exhaust_y = True
                else:
                    if r > z:
                        hy = y
                        y, exhaust_y = cal_low_high(ly, hy)
                    else:
                        ly = y
                        y, exhaust_y = cal_low_high(ly, hy)
                if exhaust_y and f(i, y) == z and [i, y] not in res:
                    res.append([i, y])
            ly, hy = 1, 1000
        return res


s = Solution()
def f(a, b):
    return a+b
# print(s.findSolution(f, 5))
# print(s.findSolution(f, 19))
# print(s.findSolution(f, 2) == [[1,1]])


def f(a, b):
    return a*b
# print(s.findSolution(f, 5))
# print(s.findSolution(f, 10))
def f(a, b):
    return a**2 + b**2
print(s.findSolution(f, 10))
