#
# @lc app=leetcode id=794 lang=python3
from collections import Counter
class Solution:
    # def validTicTacToe(self, board: List[str]) -> bool:
    def validTicTacToe(self, board):
                
        def win(board, s):
            if s in board:
                return True
            j = "".join(board)
            for i in range(3):
                if j[i] + j[i+3] +j[i+6] == s:
                    return True
            # print(j[0]+j[4]+j[8])
            # print(j[2] + j[4] + [6])
            return j[0]+j[4]+j[8] == s or j[2] + j[4] + j[6] == s


        j = "".join(board)
        jc = Counter(j)
        # print(jc)
        
        if jc['O'] > jc['X']:
            return False

        if not win(board, "XXX"):
            if jc['X'] - jc['O'] > 1:
                return False
        else:
            if jc['X'] - jc['O'] != 1:
                return False            

        if win(board, "OOO"):
            if jc['X'] > jc['O']:
                return False

        return True



# s = Solution()
# board = ["O  ", "   ", "   "]
# print(s.validTicTacToe(board) == False)
# # 
# board = ["XOX", " X ", "   "]
# print(s.validTicTacToe(board) == False)
# # 
# board = ["XXX", "   ", "OOO"]
# print(s.validTicTacToe(board) == False)
# # 
# board = ["XOX", "O O", "XOX"]
# print(s.validTicTacToe(board))


