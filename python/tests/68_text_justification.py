#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (25.80%)
# Likes:    525
# Dislikes: 1336
# Total Accepted:    119.5K
# Total Submissions: 462.8K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
# 
# Note:
# 
# 
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
# 
# 
# Example 1:
# 
# 
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be",
# because the last line must be left-justified instead of fully-justified.
# ⁠            Note that the second line is also left-justified becase it
# contains only one word.
# 
# 
# Example 3:
# 
# 
# Input:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠"understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
# 
# 
#

# @lc code=start
from pprint import pprint
class Solution:
    # def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    def fullJustify(self, words, maxWidth):
        """
        
        """
        res, line, word_length = [], [], 0
        for w in words:
            if word_length + len(w) + len(line) > maxWidth:
                # start process the filled line
                for i in range(maxWidth - word_length):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line, word_length = [], 0
            line += [w]
            word_length += len(w)
        return res + [' '.join(line).ljust(maxWidth)]
    def fullJustify_me(self, words, maxWidth):

        i = 0
        width = maxWidth
        res = []
        line = []
        while i < len(words):
            
            while i < len(words) and len(words[i]) <= width:
                line.append(words[i])
                width -= len(words[i])
                if width > 0:
                    width -= 1
                i += 1
            res.append(line)
            line = []
            width = maxWidth
        # print()
        # pprint(res, width=40)


        def get_space_width(line):
            words_total_length = sum(map(len, line))
            left_space = maxWidth - words_total_length
            if len(line) > 1:
                q, r = divmod(left_space, len(line) - 1)
            else:
                q = left_space
                r = 0
            return q, r


        def arm(line, q, r, i):
            if i == len(res) - 1:
                return " ".join(line).ljust(maxWidth, " ")
            elif len(line) == 1:
                return line[0].ljust(maxWidth, " ")
            idx = 0
            line_string = ""
            while idx < len(line) - 1:
                if r > 0:
                    line_string += line[idx] + " " * q + " "
                    r -= 1
                else:
                    line_string += line[idx] + " " * q
                idx += 1
            line_string += line[-1]
            return line_string

        for i, line in enumerate(res):
            q, r = get_space_width(line)
            # print(line, 'q=', q, 'r=', r)
            res[i] = arm(line, q, r, i)
            # print(line)
        # pprint(res)
        return res

# @lc code=end
