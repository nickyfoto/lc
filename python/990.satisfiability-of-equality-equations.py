#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (41.11%)
# Total Accepted:    10.1K
# Total Submissions: 24.5K
# Testcase Example:  '["a==b","b!=a"]'
#
# Given an array equations of strings that represent relationships between
# variables, each string equations[i] has length 4 and takes one of two
# different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not
# necessarily different) that represent one-letter variable names.
# 
# Return true if and only if it is possible to assign integers to variable
# names so as to satisfy all the given equations.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.  There is no way to assign the variables to
# satisfy both equations.
# 
# 
# 
# Example 2:
# 
# 
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# 
# 
# 
# Example 3:
# 
# 
# Input: ["a==b","b==c","a==c"]
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: ["a==b","b!=c","c==a"]
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: ["c==c","b==d","x!=z"]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='
# 
# 
# 
# 
# 
# 
# 
#
# from graph import Graph


# from coreviews import AdjacencyView
# from reportviews import NodeView
# from exception import NetworkXError
from collections.abc import Mapping
class AtlasView(Mapping):
    __slots__ = ('_atlas',)

    def __getstate__(self):
        return {'_atlas': self._atlas}

    def __setstate__(self, state):
        self._atlas = state['_atlas']

    def __init__(self, d):
        self._atlas = d

    def __len__(self):
        return len(self._atlas)

    def __iter__(self):
        return iter(self._atlas)

    def __getitem__(self, key):
        return self._atlas[key]

    def copy(self):
        return {n: self[n].copy() for n in self._atlas}

    def __str__(self):
        return str(self._atlas)  # {nbr: self[nbr] for nbr in self})

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._atlas)


class AdjacencyView(AtlasView):
    __slots__ = ()   # Still uses AtlasView slots names _atlas

    def __getitem__(self, name):
        return AtlasView(self._atlas[name])

    def copy(self):
        return {n: self[n].copy() for n in self._atlas}
class Graph:

    def __init__(self):
        self._node = {}
        self._adj = {}
        self.graph = {}
    def __iter__(self):
        return iter(self._node)

    def __len__(self):
        return len(self._node)

    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes

    @property
    def adj(self):
        return AdjacencyView(self._adj)

    def add_node(self, node_for_adding, **attr):
        if node_for_adding not in self._node:
            self._adj[node_for_adding] = {}
            attr_dict = self._node[node_for_adding] = {}
            attr_dict.update(attr)
        else:  # update attr even if node already exists
            self._node[node_for_adding].update(attr)

    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        # add nodes
        if u not in self._node:
            self._adj[u] = {}
            self._node[u] = {}
        if v not in self._node:
            self._adj[v] = {}
            self._node[v] = {}
        # add the edge
        datadict = self._adj[u].get(v, {})
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict

    def add_edges_from(self, ebunch_to_add, **attr):
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}  # doesn't need edge_attr_dict_factory
            else:
                raise NetworkXError(
                    "Edge tuple %s must be a 2-tuple or 3-tuple." % (e,))
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
        try:
            # print(self._adj)
            return iter(self._adj[n])
        except KeyError:
            raise NetworkXError("The node %s is not in the graph." % (n,))

    def is_directed(self):
        """Returns True if graph is directed, False otherwise."""
        return False

    def is_multigraph(self):
        """Returns True if graph is a multigraph, False otherwise."""
        return False

class Solution:
    # def equationsPossible(self, equations: List[str]) -> bool:
    def equationsPossible(self, equations):

        equations.sort(key=lambda x: x[1], reverse=True)
        # print(equations)
        if equations[-1][1] == '=':
            return True

        # import networkx as nx 
        # g = nx.Graph()
        g = Graph()

        def bidirectional_pred_succ(G, source, target):
            pred = {source: None}
            succ = {target: None}
            forward = [source]
            backward = [target]
            while forward and backward:
                if len(forward) <= len(backward):
                    this_level = forward
                    forward = []
                    for v in this_level:
                        for w in G.adj[v]:
                            if w not in pred:
                                forward.append(w)
                                pred[w] = v
                            if w in succ:
                                return pred, succ, w
                else:
                    this_level = backward
                    backward = []
                    for v in this_level:
                        for w in G.adj[v]:
                            if w not in succ:
                                backward.append(w)
                                succ[w] = v
                            if w in pred:
                                return pred, succ, w
            return None



        for e in equations:
            if e[1] == '=':
                u, v = e[0], e[3]
                g.add_edge(u, v)
            else:
                u, v = e[0], e[3]
                if u == v:
                    return False
                if u not in g:
                    g.add_node(u)
                if v not in g:
                    g.add_node(v)
                # if nx.has_path(g, u, v):
                if bidirectional_pred_succ(g, u, v):
                    return False
        return True





# s = Solution()
# equations = ["a==b","b!=c","c==a"]
# print(s.equationsPossible(equations) == False)

# equations = ["c==c","b==d","x!=z"]
# print(s.equationsPossible(equations))

# equations = ["b==a","a==b"]
# print(s.equationsPossible(equations))


# equations = ["a==b","b!=a"]
# print(s.equationsPossible(equations) == False)


# equations = ["a==b","b==c","a==c"]
# print(s.equationsPossible(equations))


# equations = ["a!=a"]
# print(s.equationsPossible(equations))







        
