#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
# https://leetcode.com/problems/filling-bookcase-shelves/description/
#
# algorithms
# Medium (55.81%)
# Total Accepted:    6K
# Total Submissions: 10.8K
# Testcase Example:  '[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]\n4'
#
# We have a sequence of books: the i-th book has thickness books[i][0] and
# height books[i][1].
# 
# We want to place these books in order onto bookcase shelves that have total
# width shelf_width.
# 
# We choose some of the books to place on this shelf (such that the sum of
# their thickness is <= shelf_width), then build another level of shelf of the
# bookcase so that the total height of the bookcase has increased by the
# maximum height of the books we just put down.  We repeat this process until
# there are no more books to place.
# 
# Note again that at each step of the above process, the order of the books we
# place is the same order as the given sequence of books.  For example, if we
# have an ordered list of 5 books, we might place the first and second book
# onto the first shelf, the third book on the second shelf, and the fourth and
# fifth book on the last shelf.
# 
# Return the minimum possible height that the total bookshelf can be after
# placing shelves in this manner.
# 
# 
# Example 1:
# 
# 
# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= books.length <= 1000
# 1 <= books[i][0] <= shelf_width <= 1000
# 1 <= books[i][1] <= 1000
# 
# 
#
from functools import lru_cache
class Solution:
    # def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
    def minHeightShelves(self, books, shelf_width):

        # put every book on a new shelf
        # it's height = previous total height + new book's height
        # starting from the second book
        # if shelf width permitted, move older book to this new shelf
        # it's height = max(current height, height of newly added book)
        # width = old + new book's width
        # update dp[i] with min(own dp[i], old one with new height)
        dp = [0]
        for i in range(1, len(books)+1):
            w, h = books[i-1]
            dp.append(dp[i-1] + h) # put on new shelf?
            j = i - 1
            while j > 0 and w + books[j-1][0] <= shelf_width:
                h = max(h, books[j-1][1])
                w += books[j-1][0]
                # print('i=', i, 'j=', j)
                dp[i] = min(dp[i], dp[j-1] + h)
                j -= 1
        # print(dp)
        return dp[-1]

    def minHeightShelves1(self, books, shelf_width):

        def recur(books, w, h):
            # print(books)
            total_height = 0
            while books:
                book = books[-1]
                if not w:
                    w, h = book
                    total_height += h
                    books.pop()
                else:
                    if book[1] <= h:
                        if w + book[0] <= shelf_width:
                            w += book[0]
                            books.pop()
                            if w == shelf_width:
                                w = 0
                        else:
                            w, h = 0, 0
                    else:
                        if w + book[0] <= shelf_width:
                            if len(books) != 1:
                                # print('here', book, books)   
                                # this shelf
                                # total_height + book[1] - h + recur(books[:-1])
                                # other_self
                                # total_height + recur(books)
                                here = book[1] - h + recur(books[:-1].copy(), w=w+book[0], h=book[1]) 
                                not_here = recur(books.copy(), w=0,h=h)
                                if here <= not_here:
                                    total_height += book[1] - h
                                    h = book[1]
                                    w += book[0]
                                    books.pop()
                                    if w == shelf_width:
                                        w = 0
                                else:
                                    w, h = 0, 0
                            else:
                                total_height += book[1] - h
                                w += book[0]
                                books.pop()
                                if w == shelf_width:
                                    w = 0
                        else:
                            w, h = 0, 0
            return total_height 
        return recur(books, w=0, h=0)            


    def minHeightShelves2(self, books, shelf_width):
        @lru_cache(None)
        def recur(books, w, h):
            books = list(books)
            total_height = 0
            while books:
                book = books[-1]
                if not w:
                    w, h = book
                    total_height += h
                    books.pop()
                else:
                    if book[1] <= h:
                        if w + book[0] <= shelf_width:
                            w += book[0]
                            books.pop()
                            if w == shelf_width:
                                w = 0
                        else:
                            w, h = 0, 0
                    else:
                        if w + book[0] <= shelf_width:
                            if len(books) != 1:
                                # print('here', book, books)   
                                # this shelf
                                # total_height + book[1] - h + recur(books[:-1])
                                # other_self
                                # total_height + recur(books)
                                here = book[1] - h + recur(tuple(books[:-1].copy()), w=w+book[0], h=book[1]) 
                                not_here = recur(tuple(books.copy()), w=0,h=h)
                                if here <= not_here:
                                    total_height += book[1] - h
                                    h = book[1]
                                    w += book[0]
                                    books.pop()
                                    if w == shelf_width:
                                        w = 0
                                else:
                                    w, h = 0, 0
                            else:
                                total_height += book[1] - h
                                w += book[0]
                                books.pop()
                                if w == shelf_width:
                                    w = 0
                        else:
                            w, h = 0, 0
            return total_height 

        here = books[-1][1] + recur(tuple(list(map(tuple, books[:-1].copy()))), w=books[-1][0],h=books[-1][1])
        # print(books[-1][0])
        not_here = recur(tuple(list(map(tuple, books.copy()))), w=0,h=0)
        # print(here, not_here)
        return min(here, not_here)

s = Solution()
        #[w,h]
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(s.minHeightShelves(books, shelf_width) == 6)


books = [[7,3],[8,7],[2,7],[2,5]]
shelf_width = 10
print(s.minHeightShelves(books, shelf_width) == 15) # 15


books = [[1,3],[2,4],[3,2]]
shelf_width = 6
print(s.minHeightShelves(books, shelf_width) == 4) # 4


books = [[11,83],[170,4],[93,80],[155,163],[134,118],[75,14],[122,192],[123,154],[187,29],[160,64],[170,152],[113,179],[60,102],[28,187],[59,95],[187,97],[49,193],[67,126],[75,45],[130,160],[4,102],[116,171],[43,170],[96,188],[54,15],[167,183],[58,158],[59,55],[148,183],[89,95],[90,113],[51,49],[91,28],[172,103],[173,3],[131,78],[11,199],[77,200],[58,65],[77,30],[157,58],[18,194],[101,148],[22,197],[76,181],[21,176],[50,45],[80,174],[116,198],[138,9],[58,125],[163,102],[133,175],[21,39],[141,156],[34,185],[14,113],[11,34],[35,184],[16,132],[78,147],[85,170],[32,149],[46,94],[196,3],[155,90],[9,114],[117,119],[17,157],[94,178],[53,55],[103,142],[70,121],[9,141],[16,170],[92,137],[157,30],[94,82],[144,149],[128,160],[8,147],[153,198],[12,22],[140,68],[64,172],[86,63],[66,158],[23,15],[120,99],[27,165],[79,174],[46,19],[60,98],[160,172],[128,184],[63,172],[135,54],[40,4],[102,171],[29,125],[81,9],[111,197],[16,90],[22,150],[168,126],[187,61],[47,190],[54,110],[106,102],[55,47],[117,134],[33,107],[2,10],[18,62],[109,188],[113,37],[59,159],[120,175],[17,147],[112,195],[177,53],[148,173],[29,105],[196,32],[123,51],[29,19],[161,178],[148,2],[70,124],[126,9],[105,87],[41,121],[147,10],[78,167],[91,197],[22,98],[73,33],[148,194],[166,64],[33,138],[139,158],[160,19],[140,27],[103,109],[88,16],[99,181],[2,140],[50,188],[200,77],[73,84],[159,130],[115,199],[152,79],[1,172],[124,136],[117,138],[158,86],[193,150],[56,57],[150,133],[52,186],[21,145],[127,97],[108,110],[174,44],[199,169],[139,200],[66,48],[52,190],[27,86],[142,191],[191,79],[126,114],[125,100],[176,95],[104,79],[146,189],[144,78],[52,106],[74,74],[163,128],[34,181],[20,178],[15,107],[105,8],[66,142],[39,126],[95,59],[164,69],[138,18],[110,145],[128,200],[149,150],[149,93],[145,140],[90,170],[81,127],[57,151],[167,127],[95,89]]
shelf_width = 200
print(s.minHeightShelves(books, shelf_width)) # time

        
