class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        def getList(label):
            if label == 0:
                return
            level = 1
            l = [1]
            n = 1
            while label > n:
                start = n
                n += 2**level
                end = n
                level += 1
                if level % 2 == 0:
                    l.extend(range(end, start, -1))
                else:
                    l.extend(range(start+1, end+1))
            # print(list(range(start+1, end+1)), level)
            # print(level, l)
            return l
        l = getList(label)
        # print(l)
        idx = l.index(label)
        res = [label]
        while idx != 0:
            if idx % 2 == 0:
                idx = (idx-1) // 2
            else:
                idx //= 2
            res.insert(0, l[idx])
        # print(res)
        return res

        # print(self.res)



# s = Solution()
# print(s.pathInZigZagTree(14))
# print(s.pathInZigZagTree(26))