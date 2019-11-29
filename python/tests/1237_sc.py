


class Solution:
    def findSolution(self, f, z):


        def cal_low_high(lo, hi):
            res = lo + (hi-lo) // 2
            if res == lo:
                exhausted = True
            else:
                exhausted = False
            return res, exhausted


        def update_upper(upperbound, x, y):
            if x <= upperbound[0] and y <= upperbound[1]:
                return [x, y]
            return upperbound


        def update_lower(lowerbound, x, y):
            if x >= lowerbound[0] and y >= lowerbound[1]:
                return [x, y]
            return lowerbound



        exhausted = False
        res = []
        lx, hx, ly, hy = 1, 1000, 1, 1000
        # self.upperbound = [hx, hy]
        # self.lowerbound = [lx, ly]


        def search(lx, hx, ly, hy):


            original_hy = hy
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
                            return None, None
                        # self.upperbound = update_upper(self.upperbound, x, y)
                        if not exhaust_y:
                            hy = y
                            y, exhaust_y = cal_low_high(ly, hy)
                            # if exhaust_x and exhaust_y:
                            #     print('here', x, y)
                            #     if f(x, y) != z:
                            #         return None, None
                            #     else:
                            #         return x, y
                        else:
                            # print('exhaust y')
                            hx = x
                            hy = original_hy
                            x, exhaust_x = cal_low_high(lx, hx)
                            y, exhaust_y = cal_low_high(ly, hy)
                    else:
                        if x == 1000 and y == 1000:
                            return None, None
                        # self.lowerbound = update_lower(self.lowerbound, x, y)
                        if not exhaust_y:
                            ly = y
                            y, exhaust_y = cal_low_high(ly, hy)
                            # if exhaust_x and exhaust_y:
                            #     return None, None
                        else:
                            # print('exhaust y')
                            lx = x
                            x, exhaust_x = cal_low_high(lx, hx)
                            hy = original_hy
                            y, exhaust_y = cal_low_high(ly, hy)
        x, y = search(1, 1000, 1, 1000)
        if x is None and y is None:
            return []
        if [x, y] not in res:
            res.append([x, y])
            # print(res)
            if x > 1:
                for i in range(1, 2*x-1, 2):
                    # print('i=', i)
                    x, y = search(1, i, 1, 1000)
                    if x is None and y is None:
                        continue
                    if [x, y] not in res:
                        res.append([x, y])

        return res




    def findSolution2(self, f, z):
        upperbound = [1000, 1000]
        lowerbound = [1, 1]

        def get_xy(upperbound, lowerbound):
            x = lowerbound[0] + (upperbound[0]-lowerbound[0]) // 2
            y = lowerbound[1] + (upperbound[1]-lowerbound[1]) // 2
            return x, y

        def update_upper(upperbound, x, y):
            if x <= upperbound[0] and y <= upperbound[1]:
                return [x, y]
            return upperbound


        def update_lower(lowerbound, x, y):
            if x >= lowerbound[0] and y >= lowerbound[1]:
                return [x, y]
            return lowerbound

        while upperbound != lowerbound:
            x, y = get_xy(upperbound, lowerbound)
            print(upperbound, lowerbound)
            print(x, y)
            r = f(x, y)
            if r == z:
                res.append([x, y])
                print(res)
                todo
            else:
                if r > z:
                    upperbound = update_upper(upperbound, x, y)
                else:
                    lowerbound = update_lower(lowerbound, x, y)
            # print(x, y)

s = Solution()
def f(a, b):
    return a+b
# print(s.findSolution(f, 5))
print(s.findSolution(f, 10))
# print(s.findSolution(f, 2) == [[1,1]])


def f(a, b):
    return a*b
# print(s.findSolution(f, 5))
