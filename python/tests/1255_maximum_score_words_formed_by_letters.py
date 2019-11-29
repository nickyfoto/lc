#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/
#
# algorithms
# Hard (70.84%)
# Likes:    73
# Dislikes: 4
# Total Accepted:    3.8K
# Total Submissions: 5.4K
# Testcase Example:  '["dog","cat","dad","good"]\n' +
#  '["a","a","c","d","d","d","g","o","o"]\n' +
#  '[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]'
#
# Given a list of words, list of  single letters (might be repeating) and score
# of every character.
# 
# Return the maximum score of any valid set of words formed by using the given
# letters (words[i] cannot be used two or more times).
# 
# It is not necessary to use all characters in letters and each letter can only
# be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0],
# score[1], ... , score[25] respectively.
# 
# 
# Example 1:
# 
# 
# Input: words = ["dog","cat","dad","good"], letters =
# ["a","a","c","d","d","d","g","o","o"], score =
# [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with
# a score of 23.
# Words "dad" and "dog" only get a score of 21.
# 
# Example 2:
# 
# 
# Input: words = ["xxxz","ax","bx","cx"], letters =
# ["z","a","b","c","x","x","x"], score =
# [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5)
# with a score of 27.
# Word "xxxz" only get a score of 25.
# 
# Example 3:
# 
# 
# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score =
# [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# Explanation:
# Letter "e" can only be used once.
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
# words[i], letters[i] contains only lower case English letters.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    # def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
    def maxScoreWords(self, words, letters, score):
        # print(len(letters), len(score))


        def get_score(word):
            return sum(score[ord(w) - 97] for w in word)



        def calculate_c(record, idx, current_keys):
            # print(current_keys, )
            if set(list(record['indices'].keys()) + [idx]) in current_keys:
                return False
            cp = record['c'].copy()
            new_c = Counter(words[idx])
            for k, v in new_c.items():
                cp[k] -= v
                if cp[k] < 0:
                    return False
            return cp

        c = Counter(letters)
        # the max score we can get is
        # max_score = sum(v*score[ord(k)-97] for k ,v in c.items())
        # print(max_score)

        words_scores = [get_score(word) for word in words]
        # print(words_scores)



        def get_available_words(record, current_keys):
            avialable_indices = []
            new_c_list = []
            for idx in range(n):
                if idx not in record['indices']:
                    new_c = calculate_c(record, idx, current_keys)
                    if new_c is not False:
                        avialable_indices.append(idx)
                        new_c_list.append(new_c)
            return avialable_indices, new_c_list



        n = len(words)
        record = {'indices': {}, 'score': 0, 'c': c}
        d = {}
        d[0] = [record]

        max_score = 0
        for i in range(1, n+1):
            d[i] = []
            # list of current indices
            current_keys = []
            for record in d[i-1]:
                avialable_indices, new_c_list = get_available_words(record, current_keys)
                for ci, idx in enumerate(avialable_indices):
                    new_record = {}
                    indices = record['indices'].copy()
                    indices[idx] = True
                    current_keys.append(set(indices.keys()))
                    new_record['indices'] = indices
                    new_record['score'] = record['score'] + words_scores[idx]
                    max_score = max(max_score, new_record['score'])
                    new_record['c'] = new_c_list[ci]
                    d[i].append(new_record)
            # if scores:
                # max_score = max(max_score, max(scores))
        return max_score
# @lc code=end
























