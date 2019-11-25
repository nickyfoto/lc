#
# @lc app=leetcode id=789 lang=python3

class Solution:
    # def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
    def escapeGhosts(self, ghosts, target):



        # manhattan distance to target
        me_target = sum(map(abs, target))

        # manhattan distance list of all ghosts to target
        ghost_target = [sum([abs(target[0] - g[0]), abs(target[1] - g[1])]) for g in ghosts]
        # print(mg)


        # manhanttan distance between ghost and me
        # ghost_me = [sum(g) for g in ghosts]
        # print(ghost_me)





        if all([me_target < gt for gt in ghost_target]):
            return True
        elif any([gt <= me_target for gt in ghost_target]):
            return False




# s = Solution()
# ghosts = [[1, 0], [0, 3]]
# target = [0, 1]
# print(s.escapeGhosts(ghosts, target))


# ghosts = [[1, 0]]
# target = [2, 0]
# print(s.escapeGhosts(ghosts, target)==False)

# ghosts = [[2, 0]]
# target = [1, 0]
# print(s.escapeGhosts(ghosts, target)==False)





# ghosts = [[1,9],[2,-5],[3,8],[9,8],[-1,3]]
# target = [8,-10]
# print(s.escapeGhosts(ghosts, target) == False)













        
