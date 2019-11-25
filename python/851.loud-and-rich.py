#
# @lc app=leetcode id=851 lang=python3
#



from collections import defaultdict
# from digraph import DiGraph
# from graph import Graph
# from graphviews import reverse_view
from collections.abc import Mapping, Set
class NodeView(Mapping, Set):
    __slots__ = '_nodes',

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

    def is_multigraph(self):
        """Returns True if graph is a multigraph, False otherwise."""
        return False

    def __iter__(self):
        return iter(self._node)

    def neighbors(self, n):
        try:
            # print(self._adj)
            return iter(self._adj[n])
        except KeyError:
            raise NetworkXError("The node %s is not in the graph." % (n,))

    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes


def frozen(*args, **kwargs):
    """Dummy method for raising errors when trying to modify frozen graphs"""
    raise NetworkXError("Frozen graph can't be modified")

def freeze(G):
    
    G.add_node = frozen
    G.add_nodes_from = frozen
    G.remove_node = frozen
    G.remove_nodes_from = frozen
    G.add_edge = frozen
    G.add_edges_from = frozen
    G.add_weighted_edges_from = frozen
    G.remove_edge = frozen
    G.remove_edges_from = frozen
    G.clear = frozen
    G.frozen = True
    return G


def generic_graph_view(G, create_using=None):
    if create_using is None:
        newG = G.__class__()
    else:
        newG = nx.empty_graph(0, create_using)
    if G.is_multigraph() != newG.is_multigraph():
        raise NetworkXError("Multigraph for G must agree with create_using")


    newG = freeze(newG)

    # create view by assigning attributes from G
    newG._graph = G
    newG.graph = G.graph

    newG._node = G._node
    if newG.is_directed():
        if G.is_directed():
            newG._succ = G._succ
            newG._pred = G._pred
            newG._adj = G._succ
        else:
            newG._succ = G._adj
            newG._pred = G._adj
            newG._adj = G._adj
    elif G.is_directed():
        if G.is_multigraph():
            newG._adj = UnionMultiAdjacency(G._succ, G._pred)
        else:
            newG._adj = UnionAdjacency(G._succ, G._pred)
    else:
        newG._adj = G._adj
    return newG

def reverse_view(G):
    if not G.is_directed():
        msg = "not implemented for undirected type"
        raise NetworkXNotImplemented(msg)
    newG = generic_graph_view(G)
    newG._succ, newG._pred = G._pred, G._succ
    newG._adj = newG._succ
    return newG

class DiGraph(Graph):
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
        
class Solution:
    # def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        # import networkx as nx

        # dg = nx.DiGraph()
        dg = DiGraph()

        for i, quietness in enumerate(quiet):
            dg.add_node(i, quietness = quietness)

        # for n in dg:
            # print(n, dg.nodes[n])
        # print(dg.nodes)

        dg.add_edges_from(richer)


        rdg = dg.reverse(copy=False)

        res = list(range(n))
        

        def dfs(node, person):
            # print(dg.nodes[node]['quietness'])
            explored = defaultdict(lambda: False)
            explored[node] = True
            
            def explore(node, person=person):
                # print(node)
                explored[node] = True
                if rdg.nodes[node]['quietness'] < quiet[res[person]]:
                    # print(quiet, person, res, 'node=', node)
                    # print('checking', rdg.nodes[node]['quietness'], quiet[person])
                    res[person] = node
                    # print('after', quiet, person, res)

                for neighbor in rdg.neighbors(node):
                    if not explored[neighbor]:
                        explore(neighbor, person=person)

            for neighbor in rdg.neighbors(node):
                # print(node, neighbor)
                if not explored[neighbor]:
                    explore(neighbor, person=person)

        for n in dg:
            dfs(n, person=n)
        # dfs(2, person=2)
        # print(dg.nodes[0])
        # print(res)
        return res






# s = Solution()
# richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
# quiet = [3,2,5,4,6,1,7,0]
# print(s.loudAndRich(richer, quiet) == [5,5,2,5,4,5,6,7] )


# richer = [[0,1],[1,2]]
# quiet = [1,0,2]
# print(s.loudAndRich(richer, quiet) == [0,1,1])



















        
