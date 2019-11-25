#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (35.95%)
# Total Accepted:    168K
# Total Submissions: 466.4K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
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
    def __iter__(self):
        return iter(self._node)
    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes
    def number_of_nodes(self):
        return len(self._node)

    def nbunch_iter(self, nbunch=None):
        if nbunch is None:   # include all nodes via iterator
            bunch = iter(self._adj)
        elif nbunch in self:  # if nbunch is a single node
            bunch = iter([nbunch])
        else:                # if nbunch is a sequence of nodes
            def bunch_iter(nlist, adj):
                try:
                    for n in nlist:
                        if n in adj:
                            yield n
                except TypeError as e:
                    message = e.args[0]
                    # capture error for non-sequence/iterator nbunch.
                    if 'iter' in message:
                        msg = "nbunch is not a node or a sequence of nodes."
                        raise NetworkXError(msg)
                    # capture error for unhashable node.
                    elif 'hashable' in message:
                        msg = "Node {} in sequence nbunch is not a valid node."
                        raise NetworkXError(msg.format(n))
                    else:
                        raise
            bunch = bunch_iter(nbunch, self._adj)
        return bunch
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

class OutEdgeDataView(object):
    """EdgeDataView for outward edges of DiGraph; See EdgeDataView"""
    __slots__ = ('_viewer', '_nbunch', '_data', '_default',
                 '_adjdict', '_nodes_nbrs', '_report')

    def __getstate__(self):
        return {'viewer': self._viewer,
                'nbunch': self._nbunch,
                'data': self._data,
                'default': self._default}

    def __setstate__(self, state):
        self.__init__(**state)

    def __init__(self, viewer, nbunch=None, data=False, default=None):
        self._viewer = viewer
        self._adjdict = viewer._adjdict
        if nbunch is None:
            self._nodes_nbrs = self._adjdict.items
        else:
            nbunch = list(viewer._graph.nbunch_iter(nbunch))
            self._nodes_nbrs = lambda: [(n, self._adjdict[n]) for n in nbunch]
        self._nbunch = nbunch
        self._data = data
        self._default = default
        # Set _report based on data and default
        if data is True:
            self._report = lambda n, nbr, dd: (n, nbr, dd)
        elif data is False:
            self._report = lambda n, nbr, dd: (n, nbr)
        else:  # data is attribute name
            self._report = lambda n, nbr, dd: \
                (n, nbr, dd[data]) if data in dd else (n, nbr, default)

    def __len__(self):
        return sum(len(nbrs) for n, nbrs in self._nodes_nbrs())

    def __iter__(self):
        return (self._report(n, nbr, dd) for n, nbrs in self._nodes_nbrs()
                for nbr, dd in nbrs.items())

    def __contains__(self, e):
        try:
            u, v = e[:2]
            ddict = self._adjdict[u][v]
        except KeyError:
            return False
        return e == self._report(u, v, ddict)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, list(self))

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

    dataview = OutEdgeDataView

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
    
    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            # keep all this inside try/except because
            # CPython throws TypeError on n not in self._succ,
            # while pre-2.7.5 ironpython throws on self._succ[n]
            try:
                if n not in self._succ:
                    self._succ[n] = self.adjlist_inner_dict_factory()
                    self._pred[n] = self.adjlist_inner_dict_factory()
                    attr_dict = self._node[n] = self.node_attr_dict_factory()
                    attr_dict.update(attr)
                else:
                    self._node[n].update(attr)
            except TypeError:
                nn, ndict = n
                if nn not in self._succ:
                    self._succ[nn] = self.adjlist_inner_dict_factory()
                    self._pred[nn] = self.adjlist_inner_dict_factory()
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
    def edges(self):
        return OutEdgeView(self)
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

class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    def findOrder(self, numCourses, prerequisites):
        
        prerequisites = [x[::-1] for x in prerequisites]
        # print(prerequisites)
        # DG = nx.DiGraph(prerequisites)
        
        dg = DiGraph()
        dg.add_nodes_from(range(numCourses))
        dg.add_edges_from(prerequisites)
        # print(list(reversed(list(nx.topological_sort(DG)))))
        # print('here', DG)
        # print(DG.edges)
        

        # print(DG.nodes)
        # print(DG.edges(2))
        # for n in DG:
            # print(type(n))
        # print(DG.in_degree())
        def DFSd(G):
            clock = 1
            def exploreD(G, z, visited, clock, pre, post):
                pre[z] = clock
                clock += 1
                visited[z] = True
                # for w in nx.neighbors(G, z):
                for _, w in G.edges(z):
                    if not visited[w]:
                        clock = exploreD(G, w, visited, clock, pre, post)
                post[z] = clock
                clock += 1
                return clock

            def dfsD(G, clock):
                n = G.number_of_nodes()
                pre = [None] * n
                post = [None] * n
                visited = [False] * n
                for z in G.nodes:
                # for z in range(n):
                    if not visited[z]:
                        clock = exploreD(G, z, visited, clock, pre, post)
                return pre, post
            return dfsD(G, clock)
        # pre, post = DFSd(DG)
        # print(pre)
        # print(post)
        def has_cycle(G):
            pre, post = DFSd(G)
            for z, w in G.edges:
                if post[z] < post[w]:
                    return True
            return False

        def topo(G):
            pre, post = DFSd(G)
            n = G.number_of_nodes()
            arr = [None] * (2 * n)
            for p in post:
                arr[p-1] = p
            # print(arr)
            return [post.index(x) for x in arr[::-1] if x != None]
        
        # print(topo(DG))
        # for z in G.nodes:
        # [8, 7, 2, 3, 0, 5, 1, 6, 9, 11, 10, 12, 4]
        # print((list(nx.topological_sort(DG))))


        # print(dg.edges(1))

        
        def networkxTopo(G):
            zero_indegree = [v for v, d in G.in_degree if d == 0]
            indegree_map = {v: d for v, d in G.in_degree if d > 0}
            l = []
            while zero_indegree:
                node = zero_indegree.pop()
                for _, child in dg.edges(node):
                    indegree_map[child] -= 1
                    if indegree_map[child] == 0:
                        zero_indegree.append(child)
                        del indegree_map[child]
                l.append(node)
            if indegree_map:
                # print('graph have cycle')

                return []
            return l
        # print(list(networkxTopo(dg)))


        # if has_cycle(dg):
            # return []
        # print(topo(dg))
        # return topo(dg)
        return networkxTopo(dg)
        # if topo(dg):
        #     return True
        # else:
        #     return False

s = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(s.findOrder(numCourses, prerequisites))

# numCourses = 2
# prerequisites = [[1,0]]
# print(s.findOrder(numCourses, prerequisites))