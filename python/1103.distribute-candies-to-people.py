class Solution:
    # def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        multiple = 0
        while candies > 0:
            print(candies, multiple)
            for n in range(num_people):
                if candies == 0:
                    break
                else:
                    add = (n+1) + multiple * (num_people)
                    print('add=', add)
                    if candies >= add:
                        res[n] += add #4
                        candies -= add
                    else: #candies < add:
                        res[n] += candies
                        candies = 0
            multiple += 1
        return res

# s = Solution()
# candies = 7
# num_people = 4
# print(s.distributeCandies(candies, num_people))
# candies = 10
# num_people = 3
# print(s.distributeCandies(candies, num_people))
