#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (72.03%)
# Total Accepted:    36.6K
# Total Submissions: 50.8K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Note:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
#
from collections import OrderedDict
# from digraph import DiGraph
class DiGraph:
    def __init__(self):
        self._node = {}
        self._adj = {}
        self.graph = {}
        self._pred = {}
        self._succ = self._adj

    def is_directed(self):
        """Returns True if graph is directed, False otherwise."""
        return True

    def add_node(self, node_for_adding, **attr):
        
        if node_for_adding not in self._succ:
            self._succ[node_for_adding] = {}
            self._pred[node_for_adding] = {}
            attr_dict = self._node[node_for_adding] = {}
            attr_dict.update(attr)
        else:  # update attr even if node already exists
            self._node[node_for_adding].update(attr)

    def add_edges_from(self, ebunch_to_add, **attr):
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}
            else:
                raise NetworkXError(
                    "Edge tuple %s must be a 2-tuple or 3-tuple." % (e,))
            if u not in self._succ:
                self._succ[u] = {}
                self._pred[u] = {}
                self._node[u] = {}
            if v not in self._succ:
                self._succ[v] = {}
                self._pred[v] = {}
                self._node[v] = {}
            datadict = self._adj[u].get(v, {})
            datadict.update(attr)
            datadict.update(dd)
            self._succ[u][v] = datadict
            self._pred[v][u] = datadict

    def reverse(self, copy=True):
        if copy:
            H = self.__class__()
            H.graph.update(deepcopy(self.graph))
            H.add_nodes_from((n, deepcopy(d)) for n, d in self.node.items())
            H.add_edges_from((v, u, deepcopy(d)) for u, v, d
                             in self.edges(data=True))
            return H
        return reverse_view(self)

    def successors(self, n):
        try:
            return iter(self._succ[n])
        except KeyError:
            raise NetworkXError("The node %s is not in the digraph." % (n,))
    neighbors = successors
class Solution:
    # def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    def allPathsSourceTarget(self, graph):

        n = len(graph)

        # import networkx as nx
        # dg = nx.DiGraph()
        dg = DiGraph()
        for u in range(n):
            edges = [(u,v) for v in graph[u] if graph[u]]
            if edges:
                dg.add_edges_from(edges)


        def all_path(G, src, dst):
            paths = []
            stack = [OrderedDict({src:None})]
            while stack:
                d = stack.pop()
                node, _ = d.popitem()
                d[node] = None
                for neighbor in G.neighbors(node):
                    if neighbor == dst:
                        dc = d.copy()
                        dc[dst] = None
                        paths.append(dc)
                        # print(d)
                    else:
                        if neighbor not in d:
                            dc = d.copy()
                            dc[neighbor] = None
                            # print(node, neighbor, d)
                            stack.append(dc)
                        # todo
                # print('here', node)

            return list(map(list, paths))


        return all_path(dg, 0, n-1)

s = Solution()
graph = [[1,2], [3], [3], []] 
# print(s.allPathsSourceTarget(graph))




graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(s.allPathsSourceTarget(graph))




exp = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]









        
