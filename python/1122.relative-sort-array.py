class Solution:
    # def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    def relativeSortArray(self, arr1, arr2):
        rest = [x for x in arr1 if x not in arr2]
        arr1 = [x for x in arr1 if x in arr2]
        arr1.sort(key = lambda x: arr2.index(x))
        # print(arr1)
        # print(rest)
        return arr1 + sorted(rest)
s = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(s.relativeSortArray(arr1, arr2))