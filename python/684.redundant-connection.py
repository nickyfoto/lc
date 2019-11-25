#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (53.04%)
# Total Accepted:    59.6K
# Total Submissions: 112K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
# 
# The given input is a graph that started as a tree with N nodes (with distinct
# values 1, 2, ..., N), with one additional edge added.  The added edge has two
# different vertices chosen from 1 to N, and was not an edge that already
# existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] with u < v, that represents an undirected edge connecting
# nodes u and v.
# 
# Return an edge that can be removed so that the resulting graph is a tree of N
# nodes.  If there are multiple answers, return the answer that occurs last in
# the given 2D-array.  The answer edge [u, v] should be in the same format,
# with u < v.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
# ⁠ 1
# ⁠/ \
# 2 - 3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
# ⁠   |   |
# ⁠   4 - 3
# 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
# 
# 
# 
# 
# Update (2017-09-26):
# We have overhauled the problem description + test cases and specified clearly
# the graph is an undirected graph. For the directed graph follow up please see
# Redundant Connection II). We apologize for any inconvenience caused.
# 
#
class Graph:

    
    def __init__(self):
        self._node = {}  # empty node attribute dict
        self._adj = {}

    def __iter__(self):           
        return iter(self._node)

    def add_edges_from(self, ebunch_to_add, **attr):
        
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}  # doesn't need edge_attr_dict_factory
            # print(self._node)
            if u not in self._node:
                self._adj[u] = {}
                self._node[u] = {}
            if v not in self._node:
                self._adj[v] = {}
                self._node[v] = {}
            datadict = self._adj[u].get(v, {})
            datadict.update(attr)
            datadict.update(dd)
            self._adj[u][v] = datadict
            self._adj[v][u] = datadict

    def neighbors(self, n):
        return iter(self._adj[n])



class Solution:
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    def findRedundantConnection(self, edges):

        # import networkx as nx
        from collections import defaultdict

        # G = nx.Graph()
        G = Graph()
        G.add_edges_from(edges)
        # print(nx.find_cycle(G))


        def explore(source, n):
            # if explored[n]:
                # return
            # print('exploreing', n)
            explored[n] = True
            for neighbor in G.neighbors(n):
                if cycle:
                    return
                if not explored[neighbor]:
                    edgeTo[neighbor] = n
                    explore(n, neighbor) 
                # neighbor already explored
                elif source != neighbor:
                    # cycle = []
                    x = n
                    while x != neighbor:
                        cycle.append(x)
                        # print(cycle)
                        if x in edgeTo:
                            x = edgeTo[x]
                        else:
                            break
                    cycle.append(neighbor)
                    # print(cycle)
                    return
                    # cycle.append(n)
                    # print('n=', n, 'source=', source, 'neighbor=', neighbor, cycle)
                    # cycles.append(cycle)
                    


                    # print('here', cycle)
        explored = defaultdict(lambda: False)
        edgeTo = {}
        cycle = []

        for n in G:
            if not explored[n]:    
                explore(-1, n)

        # print(cycle)
        if cycle:
            for i in range(len(edges)-1, -1, -1):
                if edges[i][0] in cycle and edges[i][1] in cycle:
                    # if abs(cycle.index(edges[i][0]) - cycle.index(edges[i][1])) == 1:
                    return edges[i]
        # else:
            # return []

# s = Solution()
# edges = [[1,2], [1,3], [2,3]]
# print(s.findRedundantConnection(edges))

# edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
# print(s.findRedundantConnection(edges))


# edges = [[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]
# print(s.findRedundantConnection(edges)) #(5,48)
# print(len(edges))
# # print(len(edge))
# for edge in edges:
#     print(edge[0]-1, edge[1]-1)







        
