#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (48.49%)
# Total Accepted:    92.8K
# Total Submissions: 190.6K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#

from functools import reduce
from operator import mul

def _bfs(G, source, target):
        q = [source]
        Gpred = G.adj
        succ = {target: None}
        while q:
            this_level = q
            q = []
            # starting from v
            for v in this_level:
                # iterate all nodes that v points to
                for w in Gpred[v]:
                    # if w is not in source
                    if w not in succ:
                        succ[w] = v
                        q.append(w)
                    if w == target:  # found path
                        succ[w] = v
                        # print('v=', v)
                        return succ, v

def bfs_shortest_path(G, source, target):

    results = _bfs(G, source, target)
    if results:
        succ, v = results
        # assemble path from target to source
        path = [target]
        while v != source:
            path.append(v)
            v = succ[v]
        path.append(source)
        path.reverse()
        return path




def shortest_path(G, source=None, target=None):
    
    paths = bfs_shortest_path(G, source, target)
    return paths

class Graph:
    pass
from collections.abc import Mapping, Set

class OutEdgeView(Set, Mapping):
    """A EdgeView class for outward edges of a DiGraph"""
    __slots__ = ('_adjdict', '_graph', '_nodes_nbrs')

    def __getstate__(self):
        return {'_graph': self._graph}

    def __setstate__(self, state):
        self._graph = G = state['_graph']
        self._adjdict = G._succ if hasattr(G, "succ") else G._adj
        self._nodes_nbrs = self._adjdict.items

    @classmethod
    def _from_iterable(cls, it):
        return set(it)

    # dataview = OutEdgeDataView

    def __init__(self, G):
        self._graph = G
        self._adjdict = G._succ if hasattr(G, "succ") else G._adj
        self._nodes_nbrs = self._adjdict.items

    # Set methods
    def __len__(self):
        return sum(len(nbrs) for n, nbrs in self._nodes_nbrs())

    def __iter__(self):
        for n, nbrs in self._nodes_nbrs():
            for nbr in nbrs:
                yield (n, nbr)

    def __contains__(self, e):
        try:
            u, v = e
            return v in self._adjdict[u]
        except KeyError:
            return False

    # Mapping Methods
    def __getitem__(self, e):
        u, v = e
        return self._adjdict[u][v]

    # EdgeDataView methods
    def __call__(self, nbunch=None, data=False, default=None):
        if nbunch is None and data is False:
            return self
        return self.dataview(self, nbunch, data, default)

    def data(self, data=True, default=None, nbunch=None):
        if nbunch is None and data is False:
            return self
        return self.dataview(self, nbunch, data, default)

    # String Methods
    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return "{0.__class__.__name__}({1!r})".format(self, list(self))
class DiGraph(Graph):
    def __init__(self, incoming_graph_data=None, **attr):
        self._node = {}
        self._pred = {}
        self._adj  = {}
        self._succ = self._adj
    def __iter__(self):
        return iter(self._node)
    def add_edge(self, u_of_edge, v_of_edge, **attr):
        
        u, v = u_of_edge, v_of_edge
        # add nodes
        if u not in self._succ:
            self._succ[u] = {}
            self._pred[u] = {}
            self._node[u] = {}
        if v not in self._succ:
            self._succ[v] = {}
            self._pred[v] = {}
            self._node[v] = {}
        # add the edge
        datadict = self._adj[u].get(v, {})
        datadict.update(attr)
        self._succ[u][v] = datadict
        self._pred[v][u] = datadict
    @property
    def adj(self):
        return self._succ
    @property
    def edges(self):
        return OutEdgeView(self)

class Solution:
    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def calcEquation(self, equations, values, queries):

        # import networkx as nx
        # dg = nx.DiGraph()
        dg = DiGraph()
        n = len(values)
        # print(edges, r_edges)
        for i in range(n):
            dg.add_edge(*equations[i], weight=values[i])
            dg.add_edge(*equations[i][::-1], weight=1.0/values[i])
        
        # for e in dg.edges:
            # print(e, dg.edges[e]['weight'])
        res = []
        for q in queries:
            # if q in dg:
            # print(q in dg.edges)
            # if q in dg.edges:
            if q[0] in dg and q[1] in dg:
                # path = nx.shortest_path(dg, *q)
                path = bfs_shortest_path(dg, *q) 
                if path:
                # print(path)
                # print(dg.edges['x1', 'x2'])
                # print(reduce(mul, (dg.edges[path[i], path[i+1]]['weight'] for i in range(len(path)-1)), 1.0))
                    res.append(reduce(mul, (dg.edges[path[i], path[i+1]]['weight'] for i in range(len(path)-1)), 1.0))
                else:
                    res.append(-1.0)
            else:
                res.append(-1.0)
        return res

# s = Solution()
# equations = [ ["a", "b"], ["b", "c"] ]
# values = [2.0, 3.0]
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]] 

# print(s.calcEquation(equations, values, queries))



# equations, values, queries = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],[3.0,0.5,3.4,5.6],[["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]
# print(s.calcEquation(equations, values, queries))

# equations, values, queries = [["a","b"],["c","d"]],[1.0,1.0],[["a","c"],["b","d"],["b","a"],["d","c"]]
# print(s.calcEquation(equations, values, queries))
