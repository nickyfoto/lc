#
# @lc app=leetcode id=1093 lang=python3
#
# [1093] Statistics from a Large Sample
#
# https://leetcode.com/problems/statistics-from-a-large-sample/description/
#
# algorithms
# Medium (44.46%)
# Total Accepted:    5.2K
# Total Submissions: 11.6K
# Testcase Example:  '[0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
#
# We sampled integers between 0 and 255, and stored the results in an array
# count:  count[k] is the number of integers we sampled equal to k.
# 
# Return the minimum, maximum, mean, median, and mode of the sample
# respectively, as an array of floating point numbers.  The mode is guaranteed
# to be unique.
# 
# (Recall that the median of a sample is:
# 
# 
# The middle element, if the elements of the sample were sorted and the number
# of elements is odd;
# The average of the middle two elements, if the elements of the sample were
# sorted and the number of elements is even.)
# 
# 
# 
# Example 1:
# Input: count =
# [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
# Example 2:
# Input: count =
# [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
# 
# 
# Constraints:
# 
# 
# count.length == 256
# 1 <= sum(count) <= 10^9
# The mode of the sample that count represents is unique.
# Answers within 10^-5 of the true value will be accepted as correct.
# 
# 
#
class Solution:
    # def sampleStats(self, count: List[int]) -> List[float]:
    def sampleStats(self, count):
        # print(len(count))
        # print(sum(count))
        def get_min(count):
            i = 0
            while count[i] == 0:
                i += 1
            return i

        def get_max(count):
            i = 255
            while count[i] == 0:
                i -= 1
            return i

        def get_mean(count):
            s = 0
            c = 0
            for i in range(mn, mx+1):
                s += i * count[i]
                c += count[i]
            # print('here', s, c)
            return s / c, c

        def get_median(count, c):
            if c % 2 == 0:
                # print(c)
                cnt = 0
                mid = c // 2
                # print('mid=', mid)
                for i in range(mn, mx+1):
                    # print('i=', i, 'count[i]=', count[i])
                    cnt += count[i]
                    if cnt >= mid:
                        # print('here i=', i, 'count[i]=', count[i])
                        if cnt == mid:
                            left = i
                            # print('left=', left)
                            right = i+1
                            # print('right=', right)
                            # print('median=', (right+left)/2)
                            return (right+left)/2
                        elif cnt > mid:
                            return i

            else:
                # print(c)
                mid = c // 2 + 1
                cnt = 0
                # print('mid=', mid)
                for i in range(mn, mx+1):
                    # print('i=', i, 'count[i]=', count[i])
                    cnt += count[i]
                    if cnt >= mid:
                        return i

        def get_mode(count):
            return mn + count[mn:mx+1].index(max(count[mn:mx+1]))

        mn = get_min(count)
        mx = get_max(count)
        mean, c = get_mean(count)
        median = get_median(count, c)
        mode = get_mode(count)
        # print(mn, mx, mean, median, mode)
        return list(map(float, [mn, mx, mean, median, mode]))


# s = Solution()
# count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print(s.sampleStats(count))



# count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print(s.sampleStats(count))

# count = [0]*256
# print(s.sampleStats(count))












