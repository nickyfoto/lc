#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#
# https://leetcode.com/problems/jump-game-iv/description/
#
# algorithms
# Hard (27.33%)
# Likes:    37
# Dislikes: 1
# Total Accepted:    1.4K
# Total Submissions: 5.1K
# Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
#
# Given an array of integers arr, you are initially positioned at the first
# index of the array.
# 
# In one step you can jump from index i to index:
# 
# 
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# 
# 
# Return the minimum number of steps to reach the last index of the array.
# 
# Notice that you can not jump outside of the array at any time.
# 
# 
# Example 1:
# 
# 
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that
# index 9 is the last index of the array.
# 
# 
# Example 2:
# 
# 
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.
# 
# 
# Example 3:
# 
# 
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last
# index of the array.
# 
# 
# Example 4:
# 
# 
# Input: arr = [6,1,9]
# Output: 2
# 
# 
# Example 5:
# 
# 
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8
# 
#

# @lc code=start

from collections import defaultdict, deque
from collections.abc import Mapping, Set
from itertools import combinations
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
    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict
    def __init__(self, incoming_graph_data=None, **attr):
        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory

        self.graph = self.graph_attr_dict_factory()   # dictionary for graph attributes
        self._node = self.node_dict_factory()  # empty node attribute dict
        self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict
        # attempt to load graph with data
        if incoming_graph_data is not None:
            convert.to_networkx_graph(incoming_graph_data, create_using=self)
        # load graph attributes (must be after convert)
        self.graph.update(attr)
    
    def __iter__(self):
        return iter(self._node)

    @property
    def adj(self):
        return AdjacencyView(self._adj)

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            # keep all this inside try/except because
            # CPython throws TypeError on n not in self._node,
            # while pre-2.7.5 ironpython throws on self._adj[n]
            try:
                if n not in self._node:
                    self._adj[n] = self.adjlist_inner_dict_factory()
                    attr_dict = self._node[n] = self.node_attr_dict_factory()
                    attr_dict.update(attr)
                else:
                    self._node[n].update(attr)
            except TypeError:
                nn, ndict = n
                if nn not in self._node:
                    self._adj[nn] = self.adjlist_inner_dict_factory()
                    newdict = attr.copy()
                    newdict.update(ndict)
                    attr_dict = self._node[nn] = self.node_attr_dict_factory()
                    attr_dict.update(newdict)
                else:
                    olddict = self._node[nn]
                    olddict.update(attr)
                    olddict.update(ndict)

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
                self._adj[u] = self.adjlist_inner_dict_factory()
                self._node[u] = self.node_attr_dict_factory()
            if v not in self._node:
                self._adj[v] = self.adjlist_inner_dict_factory()
                self._node[v] = self.node_attr_dict_factory()
            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
            datadict.update(attr)
            datadict.update(dd)
            self._adj[u][v] = datadict
            self._adj[v][u] = datadict
    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes

    def is_directed(self):
        """Returns True if graph is directed, False otherwise."""
        return False
def _bidirectional_pred_succ(G, source, target):
    # does BFS from both source and target and meets in the middle
    if target == source:
        return ({target: None}, {source: None}, source)

    # handle either directed or undirected
    if G.is_directed():
        Gpred = G.pred
        Gsucc = G.succ
    else:
        Gpred = G.adj
        Gsucc = G.adj

    # predecesssor and successors in search
    pred = {source: None}
    succ = {target: None}

    # initialize fringes, start with forward
    forward_fringe = [source]
    reverse_fringe = [target]

    while forward_fringe and reverse_fringe:
        if len(forward_fringe) <= len(reverse_fringe):
            this_level = forward_fringe
            forward_fringe = []
            for v in this_level:
                for w in Gsucc[v]:
                    if w not in pred:
                        forward_fringe.append(w)
                        pred[w] = v
                    if w in succ:  # path found
                        return pred, succ, w
        else:
            this_level = reverse_fringe
            reverse_fringe = []
            for v in this_level:
                for w in Gpred[v]:
                    if w not in succ:
                        succ[w] = v
                        reverse_fringe.append(w)
                    if w in pred:  # found path
                        return pred, succ, w

    raise nx.NetworkXNoPath("No path between %s and %s." % (source, target))

def bidirectional_shortest_path(G, source, target):

    if source not in G or target not in G:
        msg = 'Either source {} or target {} is not in G'
        raise nx.NodeNotFound(msg.format(source, target))

    # call helper to do the real work
    results = _bidirectional_pred_succ(G, source, target)
    pred, succ, w = results

    # build path from pred+w+succ
    path = []
    # from source to w
    while w is not None:
        path.append(w)
        w = pred[w]
    path.reverse()
    # from w to target
    w = succ[path[-1]]
    while w is not None:
        path.append(w)
        w = succ[w]

    return path
class Solution:
    # def minJumps(self, arr: List[int]) -> int:

    def minJumps(self, arr):
        d = defaultdict(list)
        [d[x].append(i) for i, x in enumerate(arr)]

        q = [(0,0)]
        num_met, pos_met = set(), set()
        while q:
            i, steps = q.pop(0) # state: position, step
            if i == len(arr) - 1: return steps
            num = arr[i]
            pos_met.add(i) # track explored positions
            print(d[num], (num not in num_met))
            for p in [i - 1, i + 1] + d[num] * (num not in num_met):
                if p in pos_met or not 0 <= p < len(arr): continue
                q.append((p, steps + 1))

            num_met.add(num) # track explored values
        

    def minJumps_tle(self, arr):
        
        d = defaultdict(list)
        for i, val in enumerate(arr):
            d[val].append(i)
        # print(d)
        n = len (arr)
        edges = []
        for _, v in d.items():
            edges += list(combinations(v, 2))
        for i in range(1, n - 1):
            edges += [(i-1,i), (i,i+1)]
            
        # print(edges, n)
        # import networkx as nx
        # g = nx.Graph()
        g = Graph()
        g.add_nodes_from(range(n))
        g.add_edges_from(edges)
        return len(bidirectional_shortest_path(g, 0, n - 1)) - 1
        
        
# @lc code=end
