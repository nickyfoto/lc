#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#
# https://leetcode.com/problems/online-election/description/
#
# algorithms
# Medium (48.02%)
# Total Accepted:    15.4K
# Total Submissions: 32.1K
# Testcase Example:  '["TopVotedCandidate","q","q","q","q","q","q"]\n' +
#  '[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]'
#
# In an election, the i-th vote was cast for persons[i] at time times[i].
# 
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was
# leading the election at time t.  
# 
# Votes cast at time t will count towards our query.  In the case of a tie, the
# most recent vote (among tied candidates) wins.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["TopVotedCandidate","q","q","q","q","q","q"],
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation: 
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the
# most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
# 
# 
# 
#
from bisect import bisect_right
class TopVotedCandidate:

    # def __init__(self, persons: List[int], times: List[int]):
    def __init__(self, persons, times):
        self.persons = persons
        self.records = self.generate_records()
        # print(self.records)
        self.times = times

    def generate_records(self):
        persons = self.persons
        self.n = len(persons)
        d = dict(zip(set(persons), [0]*len(set(persons))))
        self.mx = 0
        records = []
        for i in range(self.n):
            if i == 0:
                d = self.generate_record(d, i)
                records.append(d)
            else:
                d = self.generate_record(records[i-1], i)
                records.append(d)
        # print(records)
        return records

    def generate_record(self, old_d, i):
        persons = self.persons
        d = old_d.copy()
        d[persons[i]] += 1
        if d[persons[i]] > self.mx:
            self.mx = d[persons[i]]
            d['leader'] = persons[i]
        elif d[persons[i]] == self.mx:
            d['leader'] = persons[i]
        return d
    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t)
        return self.records[idx-1]['leader']


# Your TopVotedCandidate object will be instantiated and called as such:
# persons = [0,1,1,0,0,1,0]
# times = [0,5,10,15,20,25,30]
# obj = TopVotedCandidate(persons, times)

# print(obj.q(3) == 0)
# print(obj.q(12) == 1)
# print(obj.q(25) == 1)
# print(obj.q(15) == 0)
# print(obj.q(24) == 0)
# print(obj.q(8) == 1)


