#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#
# https://leetcode.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (48.66%)
# Total Accepted:    15.3K
# Total Submissions: 31.3K
# Testcase Example:  '2\n[[1,2]]'
#
# In a town, there are N people labelled from 1 to N.  There is a rumor that
# one of these people is secretly the town judge.
# 
# If the town judge exists, then:
# 
# 
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# 
# 
# You are given trust, an array of pairs trust[i] = [a, b] representing that
# the person labelled a trusts the person labelled b.
# 
# If the town judge exists and can be identified, return the label of the town
# judge.  Otherwise, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 2, trust = [[1,2]]
# Output: 2
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# 
# 
# 
# Example 4:
# 
# 
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
# 
# 
# 
# Example 5:
# 
# 
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N
# 
# 
#
from collections.abc import Mapping, Set
class NodeView(Mapping, Set):
    def __getstate__(self):
        return {'_nodes': self._nodes}

    def __setstate__(self, state):
        self._nodes = state['_nodes']

    def __init__(self, graph):
        self._nodes = graph._node

    # Mapping methods
    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __getitem__(self, n):
        return self._nodes[n]

    # Set methods
    def __contains__(self, n):
        return n in self._nodes

    @classmethod
    def _from_iterable(cls, it):
        return set(it)

    # DataView method
    def __call__(self, data=False, default=None):
        if data is False:
            return self
        return NodeDataView(self._nodes, data, default)

    def data(self, data=True, default=None):
        if data is False:
            return self
        return NodeDataView(self._nodes, data, default)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, tuple(self))

class Graph:
    def __init__(self):
        pass
    
    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes

class DiDegreeView:
    def __init__(self, G, nbunch=None, weight=None):
        self._graph = G
        self._succ = G._succ if hasattr(G, "_succ") else G._adj
        self._pred = G._pred if hasattr(G, "_pred") else G._adj
        self._nodes = self._succ if nbunch is None \
            else list(G.nbunch_iter(nbunch))
        self._weight = weight
    

    def __str__(self):
        return str(list(self))

    
class InDegreeView(DiDegreeView):
    """A DegreeView class to report in_degree for a DiGraph; See DegreeView"""

    def __getitem__(self, n):
        weight = self._weight
        nbrs = self._pred[n]
        if weight is None:
            return len(nbrs)
        return sum(dd.get(weight, 1) for dd in nbrs.values())

    def __iter__(self):
        weight = self._weight
        if weight is None:
            for n in self._nodes:
                preds = self._pred[n]
                yield (n, len(preds))
        else:
            for n in self._nodes:
                preds = self._pred[n]
                deg = sum(dd.get(weight, 1) for dd in preds.values())
                yield (n, deg)

class OutDegreeView(DiDegreeView):
    """A DegreeView class to report out_degree for a DiGraph; See DegreeView"""

    def __getitem__(self, n):
        weight = self._weight
        nbrs = self._succ[n]
        if self._weight is None:
            return len(nbrs)
        return sum(dd.get(self._weight, 1) for dd in nbrs.values())

    def __iter__(self):
        weight = self._weight
        if weight is None:
            for n in self._nodes:
                succs = self._succ[n]
                yield (n, len(succs))
        else:
            for n in self._nodes:
                succs = self._succ[n]
                deg = sum(dd.get(weight, 1) for dd in succs.values())
                yield (n, deg)

class DiGraph(Graph):
    """docstring for DiGraph"""
    def __init__(self):
        self.adjlist_outer_dict_factory = dict
        self.adjlist_inner_dict_factory = dict
        
        self.node_dict_factory = dict
        self.node_attr_dict_factory = dict
        self.edge_attr_dict_factory = dict

        self._node = self.node_dict_factory()  # dictionary for node attr
        self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict
        self._pred = self.adjlist_outer_dict_factory()  # predecessor
        self._succ = self._adj  # successor
    
    def add_edges_from(self, ebunch_to_add, **attr):
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}
            else:
                raise Exception(
                    "Edge tuple %s must be a 2-tuple or 3-tuple." % (e,))
            if u not in self._succ:
                self._succ[u] = self.adjlist_inner_dict_factory()
                self._pred[u] = self.adjlist_inner_dict_factory()
                self._node[u] = self.node_attr_dict_factory()
            if v not in self._succ:
                self._succ[v] = self.adjlist_inner_dict_factory()
                self._pred[v] = self.adjlist_inner_dict_factory()
                self._node[v] = self.node_attr_dict_factory()
            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
            datadict.update(attr)
            datadict.update(dd)
            self._succ[u][v] = datadict
            self._pred[v][u] = datadict
    @property
    def pred(self):
        return self._pred
    @property
    def succ(self):
        return self._succ
    @property
    def in_degree(self):
        return InDegreeView(self)
    @property
    def out_degree(self):
        return OutDegreeView(self)
    

# G = DiGraph()
# N = 2
# trust = [[1,2]]
# G.add_edges_from(trust)
# print("my")
# print(G.succ)
# print(G.pred)
# print(G.in_degree)
# print(G.out_degree)
# print(G.nodes)

# for n in G.nodes:
#     if G.in_degree[n] == N - 1 and G.out_degree[n] == 0:
#         print(n)
#     else:
#         print(-1)

# print('nx')
class Solution:
    # def findJudge(self, N: int, trust: List[List[int]]) -> int:

    # def findJudge(self, N, trust):
    #     judge = [p for p in range(1, N+1) if p not in [r[0] for r in trust]]
    #     if not judge:
    #         return -1
    #     # print(judge)
    #     if len([r for r in trust if r[1] == judge[0]]) < N - 1:
    #         return -1
    #     else:
    #         return judge[0]
    
    def findJudge(self, N, trust):
        # import networkx as nx
        # G = nx.DiGraph()
        if not trust:
            return 1
        G = DiGraph()
        G.add_edges_from(trust)
        # print(G.succ)
        # print(G.pred)
        # # print(G.degree)
        # print(G.in_degree)
        # print(G.out_degree)
        # print(G.nodes)
        for n in G.nodes:
            if G.in_degree[n] == N - 1 and G.out_degree[n] == 0:
                return n
            # n.get_node_attributes()
        else:
            return -1





# s = Solution()
# N = 2
# trust = [[1,2]]

# print(s.findJudge(N, trust))

# N = 3
# trust = [[1,3],[2,3]]
# print(s.findJudge(N, trust))



# N = 3
# trust = [[1,3],[2,3],[3,1]]
# print(s.findJudge(N, trust))



# N = 3
# trust = [[1,2],[2,3]]
# print(s.findJudge(N, trust))


# N = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# print(s.findJudge(N, trust))



