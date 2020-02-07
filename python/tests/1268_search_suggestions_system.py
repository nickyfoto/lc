#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
# https://leetcode.com/problems/search-suggestions-system/description/
#
# algorithms
# Medium (58.19%)
# Likes:    162
# Dislikes: 59
# Total Accepted:    13.8K
# Total Submissions: 23.7K
# Testcase Example:  '["mobile","mouse","moneypot","monitor","mousepad"]\r\n"mouse"\r'
#
# Given an array of strings products and a string searchWord. We want to design
# a system that suggests at most three product names from products after each
# character of searchWord is typed. Suggested products should have common
# prefix with the searchWord. If there are more than three products with a
# common prefix return the three lexicographically minimums products.
# 
# Return list of lists of the suggested products after each character of
# searchWord is typed. 
# 
# 
# Example 1:
# 
# 
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"],
# searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically =
# ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user
# ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
# 
# 
# Example 2:
# 
# 
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# 
# 
# Example 3:
# 
# 
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord =
# "bags"
# Output:
# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
# 
# 
# Example 4:
# 
# 
# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= products.length <= 1000
# There are no repeated elements in products.
# 1 <= Σ products[i].length <= 2 * 10^4
# All characters of products[i] are lower-case English letters.
# 1 <= searchWord.length <= 1000
# All characters of searchWord are lower-case English letters.
# 
# 
#

# @lc code=start
from pprint import pprint
class Solution:
    # def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:


    

    def suggestedProducts(self, products, searchWord):
        """
        @lee215
        """
        from bisect import bisect_left
        products.sort()
        res = []
        for i in range(1, len(searchWord) + 1):
            idx = bisect_left(products, searchWord[:i])
            # print(products[idx: idx + 3])
            res.append([p for p in products[idx: idx + 3] if p.startswith(searchWord[:i])])
        return res

    def suggestedProducts_me(self, products, searchWord):
        products.sort()
        max_length = max(map(len, products))
        # print(products, max_length)

        def get_indices(length):
            indices = {}
            for j in range(len(products)):
                if products[j][:i] not in indices:
                    indices[products[j][:i]] = [j]
                else:
                    indices[products[j][:i]].append(j)
            return indices


        indices = {}
        for i in range(1, max_length + 1):
            indices[i] = get_indices(i)
        # print(indices)

        res = []
        for i in range(1, len(searchWord) + 1):
            # print('i=', i, searchWord[:i])
            if i <= max_length:
                word_indices = indices[i]
                if searchWord[:i] in word_indices:
                    res.append([products[j] for j in word_indices[searchWord[:i]][:3]])
                else:
                    res.append([])
            else:
                res.append([])
        # pprint(res)
        return res
# @lc code=end
