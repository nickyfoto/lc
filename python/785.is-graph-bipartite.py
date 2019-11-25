#
# @lc app=leetcode id=785 lang=python3
#
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
        self._node = {}
        self._adj = {}

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


    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes

    def neighbors(self, n):
        return iter(self._adj[n])

from collections import defaultdict
class Solution:
    # def isBipartite(self, graph: List[List[int]]) -> bool:
    def isBipartite(self, graph):


        n = len(graph)
        # if n % 2 != 0:
        #     return False

        # from networkx import nx
        # g = nx.Graph()
        g = Graph()
        for u in range(n):
            for v in graph[u]:
                g.add_edge(u, v)

        # print(nx.info(g))
        red = set()
        explored = defaultdict(lambda: False)
        
        def dfs(node, set_red):
            # print('start exploring', node, 'set_red=', set_red, 'red=', red)
            explored[node] = True
            if set_red:
                red.add(node)

            for neighbor in g.neighbors(node):
                if not explored[neighbor]:
                    res = dfs(neighbor, set_red = not set_red)
                    # print('finish exploring', node, 'set_red=', set_red, 'red=', red, 'res=', res)
                    return res
                else:
                    # True means not bipartite
                    if set_red and neighbor in red:
                        # print('finish exploring', node, 'set_red=', set_red, 'red=', red, 'res=', True)
                        return True
                    elif not set_red and neighbor not in red:
                        # print('finish exploring', node, 'set_red=', set_red, 'red=', red, 'res=', True)
                        return True                

        for n in g.nodes:
            if not explored[n]:
                if all([not explored[neighbor] for neighbor in g.neighbors(n)]):
                    if dfs(n, set_red=True):
                        return False
                else:
                    for neighbor in g.neighbors(n):
                        if explored[neighbor]:
                            if neighbor in red:
                                if dfs(n, set_red=False):
                                    return False
                            else:
                                if dfs(n, set_red=True):
                                    return False
        return True




# s = Solution()
# graph = [[1,3], [0,2], [1,3], [0,2]]
# print(s.isBipartite(graph))



# graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
# print(s.isBipartite(graph) == False)




# graph = [[3],[2,4],[1],[0,4],[1,3]]
# print(s.isBipartite(graph)) #True



# graph = [[1,4],[0,2],[1],[4],[0,3]]
# print(s.isBipartite(graph)) #True








        
