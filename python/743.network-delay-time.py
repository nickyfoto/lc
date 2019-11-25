#
# @lc app=leetcode id=743 lang=python3

from heapq import heappush, heappop
class Graph:
    def __init__(self):
        self._node = {}
    def __iter__(self):
        return iter(self._node)

class DiDegreeView(object):
    def __init__(self, G, nbunch=None, weight=None):
        self._graph = G
        self._succ = G._succ if hasattr(G, "_succ") else G._adj
        self._pred = G._pred if hasattr(G, "_pred") else G._adj
        self._nodes = self._succ if nbunch is None \
            else list(G.nbunch_iter(nbunch))
        self._weight = weight

    def __call__(self, nbunch=None, weight=None):
        if nbunch is None:
            if weight == self._weight:
                return self
            return self.__class__(self._graph, None, weight)
        try:
            if nbunch in self._nodes:
                if weight == self._weight:
                    return self[nbunch]
                return self.__class__(self._graph, None, weight)[nbunch]
        except TypeError:
            pass
        return self.__class__(self._graph, nbunch, weight)

    def __getitem__(self, n):
        weight = self._weight
        succs = self._succ[n]
        preds = self._pred[n]
        if weight is None:
            return len(succs) + len(preds)
        return sum(dd.get(weight, 1) for dd in succs.values()) + \
            sum(dd.get(weight, 1) for dd in preds.values())

    def __iter__(self):
        weight = self._weight
        if weight is None:
            for n in self._nodes:
                succs = self._succ[n]
                preds = self._pred[n]
                yield (n, len(succs) + len(preds))
        else:
            for n in self._nodes:
                succs = self._succ[n]
                preds = self._pred[n]
                deg = sum(dd.get(weight, 1) for dd in succs.values()) \
                    + sum(dd.get(weight, 1) for dd in preds.values())
                yield (n, deg)

    def __len__(self):
        return len(self._nodes)

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, dict(self))
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

from collections.abc import Mapping

class AtlasView(Mapping):
    """An AtlasView is a Read-only Mapping of Mappings.

    It is a View into a dict-of-dict data structure.
    The inner level of dict is read-write. But the
    outer level is read-only.

    See Also
    ========
    AdjacencyView - View into dict-of-dict-of-dict
    MultiAdjacencyView - View into dict-of-dict-of-dict-of-dict
    """
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

class DiGraph(Graph):
    def __init__(self):
        self._adj = {}
        self._pred = {}
        self._succ = self._adj
        self._node = {}

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            if n not in self._succ:
                self._succ[n] = {}
                self._pred[n] = {}
                attr_dict = self._node[n] = {}
                attr_dict.update(attr)
            else:
                self._node[n].update(attr)

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

    def add_edge(self, u, v, **attr):
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


    def is_directed(self):
        """Returns True if graph is directed, False otherwise."""
        return True  
    @property
    def out_degree(self):
        return OutDegreeView(self)
    
    @property
    def pred(self):
        return AdjacencyView(self._pred)
    
    @property
    def succ(self):
        return AdjacencyView(self._succ)


def dijkstra(G, sources, target, paths=None):
    # paths = {source: [source]}
    
    weight = lambda u, v, data: data.get('weight', 1)
    G_succ = G._succ if G.is_directed() else G._adj

    seen = {}
    min_pq = []
    for source in sources:
        seen[source] = 0
        heappush(min_pq, (0, source))
    dist = {}
    while min_pq:
        d, v = heappop(min_pq)
        if v in dist: # already searched this node.
            continue
        dist[v] = d
        if v == target:
            break
        for u, e in G_succ[v].items():
            cost = weight(v, u, e)
            vu_dist = dist[v] + cost # single source
            if u in dist:
                if vu_dist < dist[u]:
                    raise ValueError('Contradictory paths found:',
                                     'negative weights?')
            elif u not in seen or vu_dist < seen[u]:
                seen[u] = vu_dist
                heappush(min_pq, (vu_dist, u))
                if paths:
                    paths[u] = paths[v] + [u]

    return dist

def shortest_path_length(G,
                         source=None,
                         target=None,
                         weight=None,
                         method='dijkstra'):
    return single_source_dijkstra_path_length(G, source, weight=weight)


def single_source_dijkstra_path_length(G, source, cutoff=None,
                                       weight='weight'):

    return multi_source_dijkstra_path_length(G, {source}, cutoff=cutoff,
                                             weight=weight)


def _weight_function(G, weight):
    return lambda u, v, data: data.get(weight, 1)

def multi_source_dijkstra_path_length(G, sources, cutoff=None,
                                      weight='weight'):
    # weight = _weight_function(G, weight)
    # return _dijkstra_multisource(G, sources, weight, cutoff=cutoff)
    return dijkstra(G, sources, target=None)


class Solution:
    # def networkDelayTime(self, times, N, K) -> int:
    def networkDelayTime(self, times, N, K):
        
        # import networkx as nx
        # dg = nx.DiGraph()
        
        dg = DiGraph()

        dg.add_nodes_from(range(1, N+1))
        edges = [t[:2] + [{'weight': t[2]}] for t in times]
        # print(edges)
        dg.add_edges_from(edges)
        # dist = nx.shortest_path_length(dg, source=K)
        dist = shortest_path_length(dg, source=K)


        # print(dist)
        if len(dist) < N:
            return -1
        return max([v for k,v in dist.items()])









# s = Solution()
# times = [[2,1,1],[2,3,1],[3,4,1]]
# N = 4
# K = 2
# print(s.networkDelayTime(times, N, K))


# s = Solution()
# times = [[1,2,1]]
# N = 2
# K = 2

# print(s.networkDelayTime(times, N, K))
