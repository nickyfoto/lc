#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (36.31%)
# Total Accepted:    54.4K
# Total Submissions: 149.7K
# Testcase Example:  '3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1'
#
# There are n cities connected by m flights. Each fight starts from city u and
# arrives at v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the
# destination dst, your task is to find the cheapest price from src to dst with
# up to k stops. If there is no such route, output -1.
# 
# 
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
# marked red in the picture.
# 
# 
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
# 
# 
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
# marked blue in the picture.
# 
# Note:
# 
# 
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to
# n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
# 
# 
#
from collections.abc import Mapping, Set


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

class EdgeDataView(OutEdgeDataView):
    
    __slots__ = ()

    def __len__(self):
        return sum(1 for e in self)

    def __iter__(self):
        seen = {}
        for n, nbrs in self._nodes_nbrs():
            for nbr, dd in nbrs.items():
                if nbr not in seen:
                    yield self._report(n, nbr, dd)
            seen[n] = 1
        del seen

    def __contains__(self, e):
        try:
            u, v = e[:2]
            ddict = self._adjdict[u][v]
        except KeyError:
            try:
                ddict = self._adjdict[v][u]
            except KeyError:
                return False
        return e == self._report(u, v, ddict)
class EdgeView(OutEdgeView):
    
    __slots__ = ()

    dataview = EdgeDataView

    def __len__(self):
        num_nbrs = (len(nbrs) + (n in nbrs) for n, nbrs in self._nodes_nbrs())
        return sum(num_nbrs) // 2

    def __iter__(self):
        seen = {}
        for n, nbrs in self._nodes_nbrs():
            for nbr in list(nbrs):
                if nbr not in seen:
                    yield (n, nbr)
            seen[n] = 1
        del seen

    def __contains__(self, e):
        try:
            u, v = e[:2]
            return v in self._adjdict[u] or u in self._adjdict[v]
        except (KeyError, ValueError):
            return False
class Graph:

    def __init__(self):
        self._node = {}
        self._adj = {}
        self.graph = {}
    def __iter__(self):
        return iter(self._node)

    def __len__(self):
        return len(self._node)

    def __getitem__(self, n):
        return self._adj[n]

    @property
    def nodes(self):
        nodes = NodeView(self)
        self.__dict__['nodes'] = nodes
        return nodes

    @property
    def adj(self):
        return AdjacencyView(self._adj)

    @property
    def edges(self):
        return EdgeView(self)

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

    def add_nodes_from(self, nodes_for_adding, **attr):
        for n in nodes_for_adding:
            # keep all this inside try/except because
            # CPython throws TypeError on n not in self._node,
            # while pre-2.7.5 ironpython throws on self._adj[n]
            try:
                if n not in self._node:
                    self._adj[n] = {}
                    attr_dict = self._node[n] = {}
                    attr_dict.update(attr)
                else:
                    self._node[n].update(attr)
            except TypeError:
                nn, ndict = n
                if nn not in self._node:
                    self._adj[nn] = {}
                    newdict = attr.copy()
                    newdict.update(ndict)
                    attr_dict = self._node[nn] = {}
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


# import heapq
from collections import OrderedDict
from copy import deepcopy
class Solution:
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    def findCheapestPrice2(self, n: int, flights, src: int, dst: int, K: int) -> int:

        flights = [(u,v,{'weight':e}) for u,v,e in flights]
        # from networkx import nx
        # g = nx.DiGraph()
        g = DiGraph()
        g.add_edges_from(flights)

        def my_all_path(G, source, targets, cutoff):
            targets = {targets}
            if not cutoff:
                cutoff = len(G) - 1
            visited = OrderedDict.fromkeys([source])
            stack = [iter(G[source])]
            while stack:
                children = stack[-1]
                child = next(children, None)
                if child is None:
                    stack.pop()
                    visited.popitem()
                elif len(visited) < cutoff:
                    if child in visited:
                        continue
                    if child in targets:
                        yield list(visited) + [child]
                    visited[child] = None
                    if targets - set(visited.keys()):
                        stack.append(iter(G[child]))
                    else:
                        visited.popitem()
                else:
                    for target in (targets & (set(children) | {child})) - set(visited.keys()):
                        yield list(visited) + [target]
                    stack.pop()
                    visited.popitem()




        paths = my_all_path(g, src, dst, cutoff=K+1)

        # print(list(paths))
        # print('all path finished')
        mn = float('inf')
        for path in paths:
            d = 0
            for i in range(1, len(path)):
                d += g.edges[(path[i-1], path[i])]['weight']
                if d > mn:
                    break
            mn = min(mn, d)
            # print(path)
        if mn == float('inf'):
            return -1

        return mn

    def findCheapestPrice1(self, n: int, flights, src: int, dst: int, K: int) -> int:

        flights = [(u,v,{'weight':e}) for u,v,e in flights]
        # from networkx import nx
        # g = nx.DiGraph()
        g = DiGraph()
        g.add_edges_from(flights)

        def my_all_path(G, source, target, cutoff):
            """
            stack the nodes we are gonna to iterate
            starting from source's neighbor
            if a node has no neighbor, pop this node from stack and visited
            elif len(visited) < cutoff: 
                if the neighbor of the nodes we already visited
                    continue with the next child
                if child in targets:
                    return list(visited) + [child]
                if target not in visited:
                    add iter(G[child]) to stack
                    add child to visited
            else child is not None and len(visited) >= cufoff
                if target is in set(children + child)
                    return visited
                in all calse
                remove this children from stack
                remove 
            """
            # target = {target}
            # paths = []
            mn_dist = float('inf')
            if not cutoff:
                cutoff = len(G) - 1
            visited = OrderedDict.fromkeys([source])
            
            # print(G[source])
            # print()
            # print(sorted( [(v['weight'],k) for k,v in G[source].items()], reverse=True))

            # sorted_d = sorted( (v['weight'],k) for k,v in G[source].items() )


            stack = [iter(G[source])]
            stack2 = [source]
            dist = {source: 0}
            while stack:
                # print(dist)
                children = stack[-1]
                parent = stack2[-1]
                # print(parent)
                child = next(children, None)
                # print('child=', child)
                if child is None:
                    stack.pop()
                    stack2.pop()
                    visited.popitem()
                elif len(visited) <= cutoff:
                    if child in visited:
                        # print(child, visited)
                        continue
                    elif child == target:
                        # print('here', dist)
                        if child not in dist:
                            dist[child] = dist[parent] + g.edges[(parent, child)]['weight']
                        else:
                            dist[child] = min(dist[child], dist[parent] + g.edges[(parent, child)]['weight'])
                        # mn_dist = min(mn_dist, dist[child])
                        if dist[child] < mn_dist:
                            mn_dist = dist[child]
                            # print(mn_dist)
                            # paths.extend([list(visited) + [child]])
                    if target not in visited:
                        if len(visited) < cutoff:
                            
                            if child not in dist:
                                dist[child] = dist[parent] + g.edges[(parent, child)]['weight']
                            else:
                                dist[child] = min(dist[child], dist[parent] + g.edges[(parent, child)]['weight'])
                            if dist[child] < mn_dist:
                                visited[child] = None
                                stack.append(iter(G[child]))
                                stack2.append(child)

                else:
                    stack.pop()
                    stack2.pop()
                    visited.popitem()
            if mn_dist == float('inf'):
                return -1
            # return paths, dist
            return mn_dist
        

        return my_all_path(g, src, dst, cutoff=K+1)
        # paths, dist = my_all_path(g, src, dst, cutoff=K+1)
        
        # if dst in dist:
        #     return dist[dst]
        # else:
        #     return -1



    def findCheapestPrice0(self, n: int, flights, src: int, dst: int, K: int) -> int:

        flights = [(u,v,{'weight':e}) for u,v,e in flights]
        # from networkx import nx
        # g = nx.DiGraph()
        g = DiGraph()
        g.add_edges_from(flights)
        # try:
        #     print('cycle', nx.find_cycle(g))
            
        # except Exception as e:
        #     print(e)


        def my_all_path(G, source, target, cutoff):
            
            mn_dist = float('inf')
            if not cutoff:
                cutoff = len(G) - 1
            visited = OrderedDict.fromkeys([source])
            

            sorted_d = sorted( (v['weight'],k) for k,v in G[source].items() )
            stack = [iter(sorted_d)]


            num_of_stops = 0
            stack2 = [(source, num_of_stops)]
            dist = {(source, num_of_stops): 0}
            while stack:
                children = stack[-1]
                parent, num_of_stops = stack2[-1]
                weight, child = next(children, (None, None))
                # print('parent=', parent, 'child=', child)
                # print(stack2)
                if child is None:
                    stack.pop()
                    stack2.pop()
                    visited.popitem()
                elif len(visited) <= cutoff:
                    if child in visited:
                        continue
                    elif child == target:
                        dist[ (child, num_of_stops+1) ] = dist[ (parent, num_of_stops) ] + weight
                        if dist[ (child, num_of_stops+1) ] < mn_dist:
                            mn_dist = dist[ (child, num_of_stops+1) ]
                            # print('update', mn_dist)
                    if target not in visited:
                        if len(visited) < cutoff:
                            cdist = dist[(parent, num_of_stops)] + weight
                            if cdist < mn_dist:
                                dist[ (child, num_of_stops+1) ] = cdist
                                visited[child] = None

                                sorted_child = sorted( (v['weight'],k) for k,v in G[child].items() )
                                # print('child=', child, sorted_child)
                                stack.append(iter(sorted_child))
                                stack2.append((child, num_of_stops+1))
                            # else:
                                # print('here', parent, child, cdist, weight)
                                # stack.pop()
                                # stack2.pop()
                                # break
                else:
                    stack.pop()
                    stack2.pop()

                    visited.popitem()
            if mn_dist == float('inf'):
                return -1
            # return paths, dist
            # print(dist)
            return mn_dist
        

        return my_all_path(g, src, dst, cutoff=K+1)


    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:

        flights = [(u,v,{'weight':e}) for u,v,e in flights]
        # from networkx import nx
        # g = nx.DiGraph()
        g = DiGraph()
        g.add_edges_from(flights)
        
        def my_all_path(G, source, target, cutoff):
            
            if cutoff is None:
                cutoff = len(G) - 1
            visited = OrderedDict.fromkeys([source])
            
            # print(dir(OrderedDict))
            # sorted_d = sorted( (v['weight'],k) for k,v in G[source].items() )

            # sorted_d = {k:v for v, k in sorted_d}

            stack = OrderedDict({source: G[source]})
            # print(stack[0])

            num_of_stops = 0
            ns = [num_of_stops]
            dist = {source: {num_of_stops: 0}}

            mn_dist = float('inf')

            while stack:
                # print(stack)
                parent, neighbors = stack.popitem()
                num_of_stops = ns.pop()
                if num_of_stops > cutoff:
                    continue
                if parent == dst:
                    continue
                # print(parent, neighbors, 'num_of_stops=', num_of_stops)
                # print(dist)
                # print(dist)

                if dst in neighbors:
                    # print(parent, num_of_stops)
                    cdist = dist[parent][num_of_stops] + neighbors[dst]['weight']
                    if num_of_stops <= cutoff and cdist < mn_dist:
                        mn_dist = cdist
                        # print('update mn_dist to', mn_dist)
                        if dst not in dist:
                            dist[dst] = {}
                            dist[dst][num_of_stops] = cdist
                        else:
                            dist[dst][num_of_stops] = cdist
                        # print(num_of_stops, cutoff)
                        

                        # need to confirm
                        visited[dst] = None
                        if num_of_stops == cutoff and not stack:
                            # print('here', dist)
                            return mn_dist

                # print(neighbors)
                neighbors = sorted( (v['weight'],k) for k,v in neighbors.items() )

                neighbors = {k:v for v, k in neighbors}

                # neighbors = {k:v['weight'] for k, v in neighbors.items()}


                if dst in neighbors:
                    for neighbor in neighbors:
                        # print('parent', parent, neighbor)
                        if neighbor != dst:
                            cdist = dist[parent][num_of_stops] + neighbors[neighbor]
                        if neighbor in visited:
                            
                            if cdist < min(dist[neighbor].values()):
                                dist[neighbor][num_of_stops] = cdist
                                # print('here')
                            else:
                                continue
                        if cdist < mn_dist:
                            # print('here')
                            if neighbor not in dist:
                                dist[neighbor] = {}
                                dist[neighbor][num_of_stops+1] = cdist
                            else:
                                dist[neighbor][num_of_stops+1] = cdist
                            # print('here', 'parent=', parent, 'neighbor=', neighbor, G[neighbor])
                            if neighbor not in stack: # and neighbor not in visited:
                                visited[neighbor] = None
                                stack[neighbor] = G[neighbor]
                                ns.append(num_of_stops+1)
                else:
                    for neighbor in neighbors:

                        # print('parent=', parent, 'neighbor=', neighbor)
                        cdist = dist[parent][num_of_stops] + neighbors[neighbor]
                        if neighbor in visited:
                            # print('here2', 'parent=', parent, neighbor, cdist, dist[neighbor])
                            if cdist < min(dist[neighbor].values()):
                                dist[neighbor][num_of_stops] = cdist
                                # print('here')
                            else:
                                continue
                        if cdist < mn_dist:
                            # print('parent2=', parent, 'neighbor=', neighbor)
                            # print('here')
                            if neighbor not in dist:
                                dist[neighbor] = {}
                                dist[neighbor][num_of_stops+1] = cdist
                            else:
                                dist[neighbor][num_of_stops+1] = cdist
                            # print('here', 'parent=', parent, 'neighbor=', neighbor, G[neighbor])
                            if neighbor not in stack: # and neighbor not in visited:
                                visited[neighbor] = None
                                stack[neighbor] = G[neighbor]
                                ns.append(num_of_stops+1)
                        # process()

            if mn_dist == float('inf'):
                return -1
            return mn_dist

        return my_all_path(g, src, dst, cutoff=K)

s = Solution()
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(s.findCheapestPrice(n, flights, src, dst, k) == 200)



n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(s.findCheapestPrice(n, flights, src, dst, k) == 500)


n = 5
flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst = 1
k = 1
print(s.findCheapestPrice(n, flights, src, dst, k) == -1)


n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
print(s.findCheapestPrice(n, flights, src, dst, k) == 6)


n = 5
flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2
print(s.findCheapestPrice(n, flights, src, dst, k) == 7) #7

n = 10
flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7
print(s.findCheapestPrice(n, flights, src, dst, k) == 14) #14
# print(s.findCheapestPrice(n, flights, src, dst, k))

n = 17
flights = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dst = 4
k = 13
print(s.findCheapestPrice(n, flights, src, dst, k) == 47) 



n = 94
flights = [[49,35,7292],[44,58,4164],[4,84,7244],[45,50,2445],[86,33,2878],[22,70,7119],[49,88,7034],[87,55,9088],[66,77,9317],[39,21,6740],[43,90,2273],[89,49,3806],[36,56,2541],[41,70,3767],[7,38,691],[90,41,6130],[69,22,4557],[76,5,7668],[69,41,461],[34,27,8816],[47,63,628],[63,49,2774],[7,78,8050],[26,28,3711],[73,26,7920],[25,21,3530],[62,68,2011],[48,69,9160],[53,87,5487],[58,21,9054],[20,1,3250],[34,0,5321],[39,24,6307],[11,38,8717],[3,86,8842],[0,58,3856],[62,17,7565],[41,23,8677],[79,42,8561],[2,9,8953],[66,44,7316],[60,16,8931],[83,3,8016],[82,21,8562],[49,39,2880],[64,68,3759],[16,30,3066],[29,21,8143],[54,61,1609],[89,59,6307],[74,18,991],[3,36,6409],[80,59,1593],[22,60,8148],[48,74,4628],[52,0,7238],[82,15,1593],[4,14,1448],[57,32,540],[14,37,7687],[31,57,8037],[55,70,1394],[46,33,1805],[48,76,5118],[29,74,831],[43,54,5112],[65,21,5897],[46,79,1317],[42,17,6917],[83,9,6465],[79,58,9163],[53,19,8411],[21,17,8966],[12,24,1429],[45,67,6661],[81,12,9599],[74,57,74],[71,47,3157],[89,88,7385],[86,15,6053],[56,25,5250],[2,76,4696],[32,82,2021],[32,17,8797],[26,5,3334],[72,68,3467],[8,4,4790],[17,76,2333],[19,72,5237],[35,20,1124],[90,89,3669],[83,76,6547],[3,24,5375],[65,77,9779],[92,55,5898],[31,75,5470],[92,25,2575],[27,50,1259],[53,54,5917],[55,91,8461],[8,38,4584],[73,62,2257],[21,46,9604],[1,5,1832],[12,17,5395],[90,72,5940],[60,37,9809],[49,90,6406],[58,66,7312],[18,86,8618],[36,27,7316],[0,45,5915],[26,22,8584],[90,39,2066],[84,62,2633],[79,80,5029],[44,40,2106],[64,58,9634],[41,42,9992],[83,43,3804],[33,66,7481],[87,85,723],[51,22,5310],[58,5,2587],[74,48,8051],[51,61,8946],[71,54,751],[36,2,6459],[83,66,3895],[75,49,1355],[2,71,7407],[68,14,3267],[55,92,968],[53,85,6777],[5,55,8179],[8,2,9897],[81,50,4624],[11,82,7976],[69,29,182],[59,77,7690],[90,92,1732],[81,26,8921],[58,48,2816],[48,54,8977],[12,85,8135],[2,29,6206],[44,12,5867],[23,0,6801],[86,90,7760],[63,43,8851],[35,53,6038],[8,58,4442],[11,32,8918],[63,66,1742],[28,27,8148],[83,37,6544],[77,21,150],[4,38,964],[88,63,7848],[83,11,6587],[23,10,2797],[1,44,4102],[88,26,4813],[65,76,9011],[74,40,3631],[22,16,6624],[5,33,8447],[52,61,4588],[19,7,8057],[68,31,3162],[42,27,2534],[80,88,9905],[17,46,2795],[64,12,5507],[31,77,2854],[66,71,2251],[77,34,3773],[15,87,68],[17,57,177],[7,91,1707],[31,90,9079],[7,18,1811],[18,15,785],[49,67,7372],[4,88,7587],[8,77,9740],[91,62,2947],[82,30,5483],[20,69,3522],[52,11,8166],[78,19,2834],[5,50,7234],[90,52,1016],[71,19,7084],[32,19,871],[37,68,2032],[87,6,1544],[79,48,2079],[76,58,9143],[70,40,8841],[2,15,6229],[11,87,1812],[4,64,4137],[37,64,3791],[20,78,9022],[27,41,3470],[82,6,728],[84,81,9607],[28,89,6425],[39,64,9620],[49,91,2252],[39,14,3539],[48,3,7288],[75,86,1345],[89,67,3168],[82,91,2392],[74,84,9191],[90,48,1640],[40,8,6218],[62,9,6264],[49,87,8352],[9,88,7852],[23,43,5693],[46,4,5781],[70,24,5110],[68,40,8265],[52,24,6217],[92,5,8451],[38,82,4985],[34,8,6291],[85,4,1772],[81,65,5292],[24,51,9738],[18,79,920],[51,58,9524],[68,67,776],[91,66,3791],[91,89,4605],[40,23,2374],[48,5,8439],[16,58,9752],[4,92,9213],[11,27,2543],[19,51,3307],[23,37,3033],[38,49,7861],[0,44,6097],[62,86,4870],[52,20,8101],[39,25,2696],[65,68,7592],[88,60,5843],[61,28,3588],[55,52,4699],[41,56,7362],[89,9,9086],[82,34,8569],[82,55,9656],[83,26,3179],[91,42,5744],[91,52,7771],[58,45,7506],[36,48,9610],[64,84,330],[22,59,3564],[47,42,4038],[86,30,4566],[66,39,6505],[68,17,7831],[16,5,7855],[50,7,5176],[74,31,698],[32,93,5902],[15,44,7665],[10,17,8860],[48,57,5752],[13,51,2818],[3,12,3187],[43,31,4995],[9,52,6528],[69,12,4526],[60,21,720],[65,17,9699],[17,47,4240],[50,45,3329],[17,15,6554],[48,14,5820],[12,69,1553],[12,78,212],[21,10,1185],[87,72,7499],[29,18,8043],[58,72,3528],[27,91,5545],[32,59,1299],[19,66,5417],[52,70,2499],[61,18,738],[84,9,7856],[36,77,7187],[41,8,4980],[4,6,8398],[8,1,6035],[65,24,8017],[18,52,9638],[27,2,5953],[87,59,496],[92,34,4178],[22,26,1342],[57,35,9811],[12,61,1691],[3,53,4988],[45,43,6553],[18,35,8080],[76,26,9483],[84,39,1731],[22,52,7320],[67,64,8535],[62,46,5906],[72,67,206],[37,43,7444],[10,83,7823],[60,30,7002],[47,71,6381],[78,67,6219],[67,3,4314],[42,13,5134],[85,16,8747],[54,7,4358],[33,17,5129],[6,22,4350],[78,71,7398],[29,9,1127],[67,52,4230],[71,34,6359],[24,65,5243],[19,11,4909],[28,3,2932],[85,77,5745],[64,91,8128],[57,90,3519],[80,43,9188],[93,55,8906],[44,27,2740],[31,26,182],[50,37,3893],[22,11,9967],[37,71,3946],[34,55,742],[20,23,1705],[45,28,972],[76,4,4876],[90,35,3515],[12,36,7482],[7,47,3303],[48,29,2473],[59,22,9364],[7,77,3880],[53,40,2307],[23,1,8730],[62,56,7667],[91,80,1238],[13,69,941],[66,85,8504],[37,65,7762],[47,74,9110],[14,28,9241],[60,71,5330],[33,0,3939],[67,10,1672],[7,84,9380],[54,23,321],[60,28,1292],[63,53,7375],[62,0,2858],[6,72,8011],[55,64,9581],[49,85,3734],[89,83,3668],[21,44,9624],[45,69,443],[91,72,3592],[71,51,7795],[52,23,9044],[28,2,4657],[39,35,1251],[92,71,6800],[79,78,8783],[37,36,8863],[39,60,9072],[36,20,8788],[76,52,9413],[71,53,8508],[9,90,7559],[7,71,3681],[62,25,493],[93,19,6035],[76,15,6398],[89,15,5270],[91,84,7346],[70,64,8397],[38,4,8757],[47,46,1164],[75,20,2456],[4,90,4955],[79,84,7133],[8,32,9252],[8,10,5999],[56,30,196],[3,68,8135],[42,80,695],[92,24,3159],[26,42,6264],[45,15,5625],[11,39,4778],[80,6,9341],[92,49,8021],[66,56,6835],[88,27,2973],[67,49,3455],[86,9,3249],[22,83,7835],[14,86,9683],[16,39,4533],[10,41,6001],[15,8,697],[71,63,7964],[86,46,4748],[42,3,601],[7,67,5546],[70,8,2790],[28,76,2670],[31,88,292],[48,7,581],[21,42,8858],[24,8,5634],[77,48,1543],[1,16,4850],[79,40,4226],[82,83,1071],[9,74,4393],[54,88,8963],[21,59,134],[44,10,6072],[78,87,2468],[88,51,7058],[60,33,8124],[45,56,5887],[80,28,4446],[27,39,3387],[72,23,767],[55,32,5088],[14,46,8872],[55,17,8966],[92,15,790],[28,72,3731],[33,30,1476],[15,70,5758],[86,13,6969],[79,37,2848],[66,87,583],[13,78,6787],[41,4,4147],[56,20,940],[76,17,7410],[93,10,4585],[54,31,3974],[25,66,6333],[52,2,9944],[39,43,3046],[22,45,6917],[29,47,9980],[70,10,9849],[23,51,4047],[11,36,586],[42,89,5481],[3,92,3174],[64,80,7768],[59,81,3134],[71,6,2062],[8,16,7698],[24,69,1852],[38,6,9090],[78,80,6370],[1,82,6891],[86,44,1409],[34,43,2912],[93,20,426],[65,71,5893],[80,67,743],[90,19,8223],[71,25,8881],[60,50,6491],[52,81,8115],[88,79,4551],[10,18,8376],[19,88,9164],[37,2,4425],[26,92,3358],[13,75,3828],[73,75,184],[63,33,423],[53,68,1789],[5,27,232],[10,9,6562],[23,15,4201],[85,3,5112],[45,77,2828],[89,66,255],[49,55,3777],[84,56,5875],[66,43,7310],[91,93,3158],[80,47,4465],[15,78,3404],[22,53,9160],[24,20,5902],[78,30,3798],[57,50,2414],[46,47,4037],[22,6,876],[38,39,7010],[23,73,4612],[34,83,2799],[23,36,534],[6,82,3214],[28,24,6804],[68,1,2890],[47,34,6021],[4,45,4664],[59,3,684],[87,79,5092],[76,73,6516],[27,23,6931],[52,71,3789],[38,15,8312],[43,3,8641],[83,90,6282],[35,56,5060],[61,38,37],[26,19,463],[92,89,577],[78,81,3580],[17,40,8657],[57,28,300],[31,93,7870],[21,4,320],[92,83,4483],[84,58,4738],[56,72,5564],[74,4,5232],[13,45,8656],[65,79,2835],[71,49,6174],[36,32,616],[30,86,7658],[83,92,3359],[6,54,2265],[53,27,1656],[82,43,6082],[5,1,4136],[48,28,3211],[3,0,1978],[71,43,7251],[31,32,9139],[53,42,9461],[31,67,5544],[73,49,8467],[43,57,9276],[66,42,9089],[51,0,2769],[51,54,8199],[25,11,5557],[20,57,7553],[50,77,748],[16,78,6023],[79,4,1719],[43,25,3552],[13,55,4034],[35,5,505],[34,48,5993],[36,71,3424],[48,23,8578],[43,56,7373],[63,20,9341],[16,61,7488],[85,10,8662],[4,0,7756],[17,39,3086],[5,44,4956],[80,53,1670],[75,73,3101],[86,1,516],[41,57,883],[69,39,8357],[67,90,3100],[47,9,6281],[55,24,6322],[34,76,6832],[4,63,2235],[62,57,4112],[74,62,3496],[12,0,9293],[41,19,2563],[11,7,7792],[17,78,6740],[27,12,3104],[70,86,1862],[6,83,5501],[23,40,7005],[65,23,8165],[53,55,3013],[27,65,2160],[40,18,9794],[11,53,2866],[10,77,725],[73,22,4652],[41,20,4318],[81,93,6996],[1,85,7607],[70,29,50],[73,28,1093],[92,18,9297],[85,59,5373],[46,13,7023],[31,3,6796],[21,22,3006],[49,61,7357],[64,46,9933],[46,77,9644],[8,78,127],[35,81,1091],[27,82,6102],[70,54,9799],[93,5,7912],[89,23,9984],[34,21,2564],[24,26,9757],[24,36,7059],[8,5,9831],[89,25,5315],[66,1,1152],[4,23,5922],[8,87,9562],[40,62,5796],[29,70,3726],[50,62,5419],[72,9,3344],[72,64,1783],[55,18,5835],[32,12,1369],[48,12,5624],[69,47,2452],[28,64,9105],[57,16,23],[45,42,628],[77,54,2084],[59,38,6757],[80,38,7884],[82,14,2801],[87,91,3079],[88,74,9957],[62,37,7084],[6,14,6398],[9,4,777],[3,19,6604],[75,22,7525],[77,12,1041],[22,85,4398],[74,10,3986],[84,69,5241],[51,42,9088],[15,7,5856],[63,74,8486],[64,89,6774],[7,62,7512],[63,54,6219],[35,87,4910],[56,57,5880],[45,21,1364],[93,79,3429],[31,92,2154],[71,57,6824],[55,6,3858],[73,87,6824],[20,89,1426],[50,24,8653],[39,16,3356],[22,34,4936],[54,28,9871],[69,32,9069],[10,82,336],[68,35,3608],[16,42,8553],[10,40,1501],[55,85,6114],[34,16,2539],[47,7,593],[62,43,646],[19,40,9254],[25,74,689],[78,21,3245],[3,43,7928],[78,8,4231],[68,50,854],[61,91,5620],[66,7,6927],[68,24,5570],[34,87,6529],[92,13,7754],[45,1,1874],[59,18,6758],[51,15,986],[75,58,6919],[93,1,5265],[26,17,3800],[21,0,7150],[82,44,8646],[21,45,3153],[19,82,653],[17,42,7169],[21,16,5127],[16,35,151],[34,1,7334],[74,91,1504],[8,79,2065],[44,59,7728],[78,17,5393],[12,48,4027],[29,20,1541],[56,24,7658],[31,6,2989],[16,12,1521],[50,63,3241],[21,57,1324],[73,38,2565],[8,65,2355],[80,15,5929],[36,63,3771],[44,18,8455],[20,76,194],[62,61,2896],[49,77,7623],[31,48,3743],[52,45,4059],[55,42,3025],[29,81,5007],[75,63,1350],[38,89,9646],[71,78,5442],[54,65,5538],[82,46,8172],[65,11,2195],[15,56,9798],[54,32,8816],[52,64,5603],[89,34,7410],[8,66,1140],[1,71,1199],[60,32,4627],[30,20,5169],[30,75,1569],[57,38,2318],[46,6,6655],[44,82,6313],[5,24,5445],[4,13,5950],[37,16,680],[50,29,7378],[87,73,4293],[22,18,8939],[92,74,4849],[20,67,2697],[57,83,5151],[38,30,8799],[3,38,8192],[56,48,5015],[56,22,1914],[8,54,3135],[75,52,6178],[72,80,2712],[31,13,3314],[36,19,6024],[87,43,7042],[3,8,3271],[30,84,976],[92,86,6715],[65,34,5505],[2,45,7446],[38,31,3821],[31,17,5052],[68,91,8461],[16,4,7049],[1,88,1426],[90,73,1780],[9,61,9525],[16,23,2074],[8,44,7848],[79,34,3044],[60,15,6300],[65,90,7832],[17,11,7805],[27,29,7230],[28,90,2736],[86,8,1904],[44,15,3032],[16,52,2468],[77,63,3605],[48,77,7243],[11,1,118],[37,61,8774],[55,44,4190],[28,40,8388],[50,51,5033],[20,48,4834],[5,9,6872],[85,29,1916],[39,13,6921],[70,93,2229],[36,85,4961],[29,55,3590],[43,86,1676],[51,12,3356],[92,88,8113],[65,28,16],[26,89,8582],[44,50,2096],[57,86,8747],[79,64,9943],[11,13,7468],[75,56,556],[0,41,9136],[6,11,3943],[88,34,3760],[91,88,1428],[35,41,9426],[1,80,7797],[16,83,2025],[21,62,9895],[65,40,9989],[87,14,7947],[26,85,8030],[18,93,2169],[46,51,5907],[50,22,5527],[76,37,3764],[4,77,6194],[38,27,1492],[7,12,8487],[31,74,1796],[0,76,4305],[86,27,3280],[24,33,3827],[70,61,1882],[82,33,3148],[90,26,7760],[62,3,618],[56,38,5263],[84,91,4302],[60,8,4688],[75,91,625],[73,52,7451],[51,62,9946],[41,45,2772],[5,79,7890],[8,26,2395],[77,5,6167],[37,83,1540],[48,85,8513],[74,20,9674],[38,40,8150],[84,1,2022],[26,51,6110],[84,90,8790],[84,41,6693],[67,13,1475],[2,19,6362],[59,48,9913],[87,88,2500],[22,74,8161],[25,51,8174],[6,38,8595],[28,53,9064],[58,65,3982],[93,61,4299],[64,81,763],[47,11,943],[16,54,8197],[70,14,846],[50,60,4343],[34,42,4776],[14,81,5677],[32,63,2266],[93,2,8007],[68,45,3425],[79,0,6924],[12,32,241],[43,37,4159],[33,18,4047],[32,16,4572],[29,30,8579],[43,14,2752],[85,47,3313],[57,51,1550],[55,5,3194],[44,29,3044],[68,76,1783],[16,81,5214],[14,7,8230],[35,90,2358],[16,57,7331],[72,19,7369],[9,27,4448],[77,19,1303],[26,44,1026],[42,70,4965],[88,46,8279],[32,57,164],[10,19,1512],[35,10,7549],[50,76,7009],[7,86,3255],[77,75,6997],[22,33,7992],[2,52,1055],[50,68,6643],[42,28,6344],[31,44,67],[31,43,8616],[67,66,3893],[73,2,1956],[13,72,8630],[47,12,187],[55,23,2313],[20,84,3939],[63,56,3365],[48,9,474],[61,73,110],[10,45,467],[16,75,1287],[0,13,1094],[88,35,3846],[32,26,7398],[13,38,4178],[65,48,6103],[50,73,6636],[71,81,6809],[46,63,9158],[59,16,1460],[22,43,7883],[60,39,4940],[60,29,6958],[61,48,6967],[58,93,7823],[2,62,3859],[41,6,7660],[79,22,6699],[29,17,4999],[46,21,8069],[24,64,8320],[21,91,8084],[19,80,7828],[31,81,1174],[75,34,9046],[81,19,7835],[92,73,9057],[50,70,7294],[21,74,3846],[87,78,8753],[21,38,9223],[72,50,6308],[10,61,5782],[44,51,4680],[14,45,5269],[91,53,6083],[30,19,4784],[84,87,5890],[45,41,8095],[20,44,1071],[62,53,5582],[47,82,86],[20,65,8481],[76,77,7988],[20,34,8432],[36,18,741],[26,1,8379],[16,85,5629],[4,17,3978],[71,84,2711],[33,36,1784],[39,2,4614],[36,5,1829],[85,43,2300],[84,23,9020],[77,67,9747],[62,29,2070],[35,47,1598],[46,87,5034],[18,14,5333],[24,11,2796],[67,54,1679],[54,4,2779],[87,13,7418],[80,91,6028],[46,22,9202],[33,43,7505],[62,76,150],[27,4,4267],[64,11,3794],[79,15,3460],[7,39,6708],[60,36,5615],[0,82,1281],[85,76,8696],[20,15,2493],[86,22,4331],[83,59,3316],[32,29,7544],[8,31,5826],[80,52,4987],[90,49,1108],[38,65,3991],[62,41,5567],[56,74,9399],[6,87,740],[18,55,2541],[13,29,9528],[71,7,4592],[38,25,6013],[4,66,2368],[67,35,3969],[3,40,3831],[6,86,367],[45,13,5925],[28,14,2243],[4,73,9009],[42,78,8095],[4,11,1282],[33,47,1853],[29,85,7967],[18,11,8629],[29,7,4231],[73,92,159],[44,89,2351],[59,64,4960],[39,91,7687],[12,45,7980],[42,77,9743],[36,12,9657],[9,57,8633],[36,91,9792],[65,2,9661],[51,34,2061],[74,25,9559],[90,27,8608],[12,6,2409],[13,49,2913],[10,29,1290],[5,43,6681],[80,14,7020],[49,11,1913],[79,52,8039],[64,79,9488],[35,89,9289],[69,44,1133],[69,53,5518],[41,31,1085],[79,9,8239],[93,22,503],[60,27,6196],[42,49,7021],[75,24,5632],[55,80,1264],[7,93,9852],[10,31,8708],[67,71,4379],[62,89,5893],[75,21,4837],[3,66,5419],[27,19,4869],[33,90,4338],[74,19,349],[55,77,8574],[22,28,5753],[88,16,7843],[1,35,3422],[57,59,8314],[45,62,9597],[20,90,977],[50,57,9169],[6,90,19],[43,74,9927],[60,22,1563],[2,93,7486],[29,77,2234],[19,32,1804],[46,20,5984],[83,86,3694],[40,47,1225],[12,16,2488],[68,7,762],[81,73,5805],[71,12,3990],[32,67,6344],[42,39,8063],[66,3,4404],[51,74,817],[42,22,1424],[4,87,6804],[70,31,7121],[45,20,7955],[20,59,497],[64,48,63],[72,78,4460],[79,82,1493],[44,54,231],[83,0,7595],[82,23,9567],[44,91,1598],[3,78,9643],[43,51,9834],[54,6,6335],[16,65,2898],[36,90,9682],[37,26,6994],[38,28,8159],[55,20,8718],[59,83,4501],[82,67,7558],[10,88,7874],[77,36,5890],[16,15,3288],[26,47,3129],[3,84,4623],[82,63,9855],[38,87,9750],[24,9,5179],[86,16,7016],[11,67,6360],[20,25,7933],[61,57,3960],[11,50,5666],[84,72,6084],[45,12,2656],[77,71,5349],[20,83,4658],[32,9,2594],[76,82,191],[69,13,1738],[0,93,8853],[15,30,181],[71,21,8764],[50,0,1626],[82,31,1338],[44,47,1811],[64,16,948],[17,25,5035],[88,20,1195],[28,29,6923],[30,39,1660],[35,76,4510],[64,26,4021],[92,10,7344],[64,14,3555],[92,9,8493],[5,0,8956],[77,41,5146],[3,7,4581],[63,14,8443],[61,65,1795],[2,65,4449],[79,23,7710],[62,8,2962],[15,31,3852],[6,76,3333],[72,86,3406],[19,43,5819],[28,30,3118],[1,42,5871],[24,45,6333],[15,46,5288],[41,38,4243],[63,46,7882],[9,17,6787],[77,35,2560],[35,3,9823],[38,26,7542],[39,44,7377],[80,90,7932],[14,22,9648],[92,28,8182],[69,21,9684],[43,71,8020],[61,32,4297],[17,26,4600],[47,15,1769],[10,8,2453],[47,22,5732],[35,8,7830],[88,13,4730],[26,27,1991],[18,53,2728],[18,26,384],[65,10,6587],[22,89,7256],[62,35,876],[18,33,3019],[69,73,8700],[49,46,5996],[58,12,6676],[88,56,420],[71,77,3192],[15,80,3081],[13,40,6878],[13,3,6471],[10,3,5148],[9,70,6643],[16,51,1134],[26,71,8],[77,93,5032],[9,89,6006],[10,91,8176],[52,87,4169],[36,62,3326],[65,93,349],[56,53,8853],[44,67,8929],[59,26,607],[77,15,1533],[52,28,7720],[59,37,51],[2,49,6947],[85,61,4386],[91,87,2903],[22,54,9380],[87,92,3300],[91,57,3919],[11,29,4005],[10,21,9697],[68,8,9710],[88,22,2698],[77,23,7820],[42,61,5890],[14,75,2001],[25,61,8107],[63,28,8005],[27,69,1198],[58,82,8790],[17,83,2170],[17,56,2413],[80,10,1149],[41,83,4410],[85,8,6176],[37,24,936],[11,33,3693],[26,60,7683],[93,16,3457],[58,3,2222],[69,20,6822],[55,15,6820],[16,41,6355],[53,11,979],[54,21,7095],[23,84,2801],[84,16,9246],[20,30,3890],[73,44,2505],[67,0,1840],[65,67,8429],[53,18,1757],[76,54,8334],[16,59,1010],[46,75,6930],[10,74,3021],[8,47,3333],[40,10,8655],[57,77,1445],[18,31,3844],[92,20,8229],[27,24,4290],[4,8,2868],[67,36,4812],[23,47,1813],[76,60,1735],[50,64,5023],[54,0,2186],[61,6,1427],[53,65,5639],[13,39,1157],[11,35,5936],[75,87,5857],[30,73,8016],[6,49,4947],[81,56,5649],[33,71,5954],[39,4,4621],[13,68,4873],[22,15,6749],[83,71,2834],[2,37,6737],[25,0,2390],[7,81,822],[16,24,3088],[68,34,3170],[11,6,6447],[85,19,191],[81,1,7210],[46,36,5833],[70,19,2770],[15,35,8931],[44,56,3570],[3,13,7793],[9,5,1312],[18,75,8362],[18,89,7018],[90,22,4021],[42,60,9538],[62,69,6215],[12,15,8805],[58,64,6186],[45,76,1657],[36,83,3843],[24,75,7955],[6,27,2988],[47,73,7636],[18,54,5411],[36,55,7227],[37,4,8956],[48,55,9443],[70,67,6258],[8,93,815],[34,7,533],[77,88,3274],[55,61,5775],[60,17,2739],[18,82,3239],[24,81,9608],[73,66,2975],[18,25,4621],[21,19,8984],[18,46,8842],[30,9,5173],[42,50,831],[32,79,7625],[30,67,5610],[51,45,8270],[49,48,6689],[87,20,9409],[62,50,7274],[46,92,7],[31,0,8075],[74,0,9598],[6,47,7579],[56,88,4308],[93,63,7482],[66,20,240],[2,80,4267],[33,37,8073],[40,16,7559],[69,16,9317],[83,23,841],[36,73,410],[69,25,9326],[6,52,5937],[58,2,1162],[7,76,6942],[2,41,3301],[30,78,4846],[37,51,4917],[78,75,9329],[7,75,4455],[81,32,9773],[56,5,8707],[31,15,5114],[3,46,1788],[64,71,119],[64,65,467],[15,62,9860],[44,69,379],[86,50,4805],[82,81,5004],[47,30,7380],[82,69,6799],[46,28,4810],[67,48,1839],[24,40,4783],[81,71,6341],[44,73,1512],[26,81,4754],[85,30,376],[58,26,9482],[21,89,914],[25,91,2997],[63,55,2349],[4,29,2248],[48,17,1498],[15,51,3834],[75,64,1905],[50,55,850],[63,68,3894],[78,88,2027],[12,62,3445],[91,41,5478],[8,34,5153],[62,60,1408],[90,55,8228],[77,66,7796],[42,66,7263],[19,84,4902],[58,33,3285],[16,70,2370],[82,56,3756],[48,82,3604],[26,14,2891],[61,51,8659],[23,87,2466],[83,19,7398],[66,58,9264],[93,51,9529],[7,56,8404],[82,22,784],[18,20,704],[11,2,4082],[28,85,4578],[58,90,6898],[34,39,3839],[28,12,3499],[81,85,5570],[36,47,3342],[93,62,2595],[89,41,2745],[29,54,5081],[69,28,5547],[18,66,7536],[29,78,791],[41,16,8298],[67,85,8456],[20,81,6625],[91,35,9365],[67,88,2919],[88,76,8895],[15,37,8104],[38,62,6126],[73,4,2397],[71,28,4129],[24,66,1642],[64,38,3925],[56,44,8555],[71,38,9572],[86,80,2946],[44,21,4620],[27,20,754],[81,41,3455],[70,50,8252],[39,75,4869],[51,76,1790],[67,27,6705],[82,47,5952],[80,70,1176],[73,58,7627],[51,47,2316],[43,34,7280],[17,18,938],[13,47,1320],[19,91,55],[25,18,9383],[39,63,8920],[89,28,3595],[60,84,3192],[58,79,7013],[65,54,5082],[41,50,269],[3,58,6389],[31,50,2161],[42,85,8292],[38,24,4364],[75,41,947],[21,75,384],[87,27,9706],[69,45,9090],[48,67,1736],[60,83,6177],[76,53,1400],[93,59,8232],[92,80,7412],[33,49,7300],[69,72,8099],[89,48,3558],[48,10,1267],[69,80,4652],[38,67,2478],[18,42,3991],[41,22,6889],[35,11,9021],[58,7,9685],[51,80,5799],[70,56,2017],[72,59,1573],[73,37,1136],[23,86,9164],[2,7,7901],[23,63,7451],[85,36,2352],[89,26,7355],[5,7,1758],[66,32,4749],[31,68,9854],[74,8,9179],[59,60,2304],[87,42,1867],[90,78,4179],[56,89,4007],[45,88,8597],[5,58,3011],[85,65,8082],[29,45,7110],[90,36,4327],[3,85,1925],[45,26,8071],[89,93,2739],[30,33,4187],[50,14,2470],[7,20,4814],[3,9,2496],[36,34,3637],[68,77,4626],[37,56,8225],[81,48,4551],[40,59,5890],[68,46,5273],[61,79,1591],[41,73,583],[57,41,4151],[1,7,8339],[53,49,3135],[72,18,5053],[37,54,9922],[28,47,1013],[69,87,8768],[4,22,4994],[78,22,5122],[17,54,2232],[92,45,5137],[20,39,1222],[12,13,2926],[75,38,2666],[86,2,871],[13,19,965],[79,39,398],[56,13,6821],[5,6,2513],[72,17,309],[25,8,9136],[22,55,1672],[15,91,3131],[42,67,5625],[53,59,4505],[42,26,1125],[22,41,403],[59,2,5688],[78,26,9220],[84,46,8995],[14,76,4838],[3,81,326],[79,85,5240],[38,57,9950],[22,81,5472],[0,17,1450],[30,82,4594],[73,25,2272],[23,75,8259],[54,20,6773],[4,33,6094],[19,49,3238],[31,11,5167],[64,70,1446],[64,40,3607],[11,3,486],[83,24,1535],[32,54,3226],[88,41,1679],[47,83,7596],[26,15,841],[55,66,3226],[38,42,5703],[86,83,7940],[8,59,6847],[24,60,5666],[80,40,2666],[10,13,9490],[21,92,736],[29,63,2475],[47,87,1989],[88,3,8718],[66,86,8771],[86,82,947],[13,8,1772],[26,56,4627],[60,53,3893],[63,93,9156],[44,3,609],[93,0,8363],[62,87,9714],[93,13,6617],[89,20,8447],[89,17,5897],[29,41,9106],[5,69,6053],[61,68,970],[54,39,2104],[24,6,6282],[0,83,8291],[85,64,1026],[31,8,3707],[74,44,1246],[68,65,205],[10,32,551],[6,88,6568],[33,48,767],[58,43,7459],[5,30,2714],[61,40,2619],[40,30,87],[55,51,6403],[17,3,3825],[34,5,6669],[5,59,471],[15,12,1087],[19,34,4354],[85,51,6276],[7,30,3818],[20,26,9053],[73,24,7784],[70,3,1086],[78,92,9626],[88,67,3884],[4,56,1594],[74,79,2442],[76,22,3568],[56,29,2112],[23,90,6041],[16,71,6004],[85,40,9270],[86,91,3383],[74,53,8819],[24,37,3784],[29,22,8087],[21,41,8383],[62,21,3621],[35,2,9459],[19,77,7921],[4,55,109],[4,48,5322],[60,85,2514],[14,77,2074],[8,7,3407],[32,72,79],[78,51,2498],[4,35,8609],[68,41,277],[79,47,9535],[93,80,3726],[12,52,8354],[82,26,7087],[17,7,5482],[73,51,1498],[2,30,8505],[22,20,2824],[38,52,5330],[89,46,5724],[18,37,7018],[93,71,6344],[34,74,1488],[5,92,722],[68,36,8563],[23,91,5672],[57,69,1086],[13,50,2610],[33,79,3642],[43,11,4581],[68,10,6432],[13,27,6324],[31,76,4123],[16,40,1644],[81,8,900],[15,79,9457],[72,49,726],[30,27,2160],[34,20,1696],[43,16,5962],[16,25,9006],[6,75,1549],[57,76,1626],[22,5,3511],[18,77,2408],[31,16,1956],[88,43,7381],[20,86,3636],[88,15,1170],[45,17,4420],[88,89,2076],[20,7,6221],[15,36,5311],[47,55,8327],[51,55,9528],[17,12,2111],[85,0,440],[80,12,2634],[80,64,3610],[22,51,6938],[90,17,2173],[65,42,33],[81,74,3817],[31,65,591],[7,49,7146],[59,15,2966],[5,64,4682],[34,19,1013],[25,57,7546],[52,49,681],[38,45,6625],[93,64,9255],[8,72,1554],[75,71,835],[12,14,5251],[1,52,5950],[68,81,970],[59,85,1032],[59,12,651],[4,58,3454],[73,33,8988],[56,3,1156],[2,54,8239],[25,70,2070],[17,71,1784],[61,10,4416],[24,84,6601],[45,32,8671],[31,5,3453],[56,32,4946],[91,73,6565],[84,78,9199],[36,7,1942],[59,8,7249],[7,48,2439],[35,66,1278],[2,35,4380],[43,40,1988],[65,44,3473],[82,79,2656],[28,33,4567],[42,72,8103],[49,58,5840],[42,46,8521],[37,79,4373],[84,64,8201],[47,10,8719],[36,80,302],[49,30,8587],[41,44,6644],[43,59,2124],[72,4,9648],[58,60,582],[65,22,5247],[17,92,7391],[79,69,1796],[28,18,8939],[75,6,8880],[27,22,4122],[4,75,97],[84,7,3202],[49,33,5428],[12,21,3519],[17,86,5461],[75,4,9725],[62,90,9767],[61,30,1849],[73,53,6714],[70,4,9721],[92,69,6693],[39,29,5556],[77,69,4305],[33,63,484],[40,64,2581],[36,64,4499],[67,19,5316],[12,51,9708],[44,57,9936],[0,79,3910],[53,51,2386],[84,50,5522],[53,7,3970],[35,52,4988],[61,0,1796],[15,84,9039],[49,50,5267],[65,7,8066],[64,67,2130],[45,59,5967],[85,75,2723],[92,43,6683],[62,14,3073],[1,73,6388],[85,37,8495],[43,75,318],[84,63,6348],[87,28,1571],[6,32,4568],[65,80,3570],[56,35,2686],[85,68,7414],[39,85,3764],[91,13,6340],[44,22,5971],[91,77,2025],[61,88,4193],[70,25,1130],[50,41,6307],[34,71,1178],[42,76,477],[92,81,3382],[64,92,5417],[20,24,3262],[58,85,4285],[57,23,3547],[22,21,7368],[59,73,5536],[23,8,8502],[55,38,9526],[77,64,1253],[68,90,9226],[80,11,9211],[73,56,3117],[9,58,1880],[45,83,7368],[92,0,7508],[17,4,9539],[67,51,7458],[58,67,1310],[61,59,5464],[4,61,5785],[26,93,4683],[79,16,4964],[47,35,5031],[91,56,3058],[28,32,32],[70,81,1569],[27,25,3352],[51,48,8039],[49,81,4520],[76,1,6992],[60,25,1495],[0,80,1162],[92,12,9755],[40,22,6731],[87,11,5318],[37,62,1708],[19,58,5064],[77,17,2103],[62,30,869],[82,38,3559],[10,70,6827],[58,70,1605],[89,64,2633],[28,70,3700],[57,4,768],[92,23,9803],[11,73,5880],[14,56,3245],[9,81,25],[3,73,756],[32,35,8992],[61,33,9607],[12,63,8802],[72,77,1204],[12,54,6300],[63,71,500],[65,88,7476],[7,6,7134],[75,17,8300],[40,21,3401],[48,93,3916],[92,1,8908],[64,23,4660],[32,15,216],[21,33,9217],[48,51,2087],[76,67,6999],[18,57,2124],[82,65,2106],[30,41,885],[39,7,1098],[8,25,1906],[72,7,1139],[62,59,8981],[52,17,9237],[89,58,1951],[39,9,2620],[14,26,8284],[87,62,8082],[30,81,5377],[86,77,4414],[20,62,2334],[32,4,9413],[54,57,8784],[9,82,784],[87,90,3037],[36,14,3227],[67,57,7988],[0,89,1953],[31,52,3296],[33,46,3536],[33,50,2688],[54,56,7095],[83,54,9253],[34,65,9274],[22,68,9476],[39,38,4345],[60,69,2448],[46,19,5419],[79,13,9450],[26,18,5064],[79,73,9879],[83,89,9901],[24,22,171],[2,17,1423],[77,51,8273],[77,1,2797],[89,74,5808],[39,15,2316],[29,71,2190],[9,78,3672],[3,70,8516],[54,50,3475],[88,58,8224],[80,87,7355],[82,84,7873],[92,59,1313],[68,38,1912],[76,87,9577],[84,66,3528],[71,4,4326],[28,8,8573],[27,63,1536],[14,66,3909],[30,40,41],[24,46,9297],[28,38,1687],[56,36,7071],[34,61,4012],[8,29,5608],[13,61,9394],[87,4,635],[8,20,2827],[50,15,5684],[28,10,6598],[25,78,5860],[48,63,6211],[33,72,3938],[90,1,2324],[80,54,3862],[26,16,8742],[12,27,1196],[16,46,60],[91,14,7110],[61,82,6555],[11,15,7290],[85,11,7788],[64,50,2402],[69,33,2118],[53,61,7983],[30,5,9186],[21,18,6617],[56,4,7601],[65,16,3151],[16,18,4435],[38,11,3584],[57,52,9937],[8,22,6591],[80,55,913],[59,31,9013],[69,49,1999],[86,53,7691],[1,4,1312],[84,38,5753],[81,38,6331],[92,91,4768],[68,44,3079],[45,16,5074],[56,79,3055],[93,41,4886],[41,80,6771],[36,21,7240],[72,61,8950],[72,16,1783],[28,67,6289],[16,37,341],[9,0,4182],[82,0,4779],[86,48,5652],[93,53,9017],[25,56,1813],[22,82,613],[42,0,30],[60,92,3541],[46,18,3588],[7,14,3403],[23,2,4178],[20,45,9039],[44,53,600],[92,19,1822],[55,3,6357],[58,16,966],[86,72,8711],[90,16,2505],[33,1,2657],[60,59,979],[13,44,5004],[7,44,4499],[29,69,7857],[65,5,6318],[33,41,9979],[38,29,4766],[80,68,3198],[69,62,3423],[27,85,2911],[70,0,1387],[4,25,56],[3,82,6423],[2,84,371],[80,1,7350],[0,4,4735],[70,23,324],[24,0,1786],[50,43,7590],[67,63,5277],[39,0,865],[32,53,6056],[0,43,2902],[77,56,5862],[44,55,3951],[8,76,8897],[37,60,570],[78,3,1584],[53,67,6136],[23,28,6649],[18,12,1301],[58,6,6524],[17,85,8911],[35,62,3343],[90,14,5289],[83,18,5587],[78,86,7921],[69,77,2355],[67,84,1519],[30,57,9594],[88,57,7874],[90,42,1890],[7,16,7275],[33,26,7506],[9,72,493],[21,36,1231],[33,75,6167],[87,67,2267],[88,23,5078],[48,90,7430],[47,61,9156],[40,50,3911],[64,88,5027],[63,6,5479],[77,59,9813],[48,81,665],[70,9,4138],[53,4,6107],[69,88,6516],[72,87,7442],[68,28,23],[16,22,5915],[87,16,3196],[31,82,5299],[40,12,9579],[19,68,5240],[0,85,8922],[52,18,2204],[14,31,5061],[62,71,8083],[54,48,6206],[5,47,7305],[19,38,5448],[91,2,9458],[47,50,5420],[5,12,11],[15,9,3128],[87,60,9344],[80,39,3756],[7,52,4920],[85,34,9602],[25,54,9145],[10,0,599],[26,20,7554],[11,78,9812],[16,45,5084],[54,83,8439],[82,5,4923],[17,35,4606],[71,73,3256],[74,30,1295],[22,90,735],[36,15,1654],[36,52,2450],[55,30,6871],[85,41,9049],[1,11,5246],[79,87,1967],[3,71,7312],[6,2,7110],[9,55,9817],[76,44,5372],[39,50,9218],[80,13,2397],[38,12,4987],[83,81,6293],[29,79,414],[8,13,3461],[50,82,7409],[7,89,4617],[20,28,3203],[54,17,1739],[74,77,8220],[43,36,7173],[13,82,4657],[56,55,2495],[11,24,9205],[41,51,4239],[73,43,4360],[8,41,9006],[78,62,1126],[14,72,5202],[13,57,4833],[10,35,3129],[71,88,4213],[3,89,8667],[23,14,8114],[90,28,1254],[43,12,6361],[81,80,8190],[17,90,4233],[53,74,3206],[30,58,3266],[91,25,5713],[77,10,4445],[28,51,9641],[59,45,6820],[46,69,4545],[72,37,5017],[73,77,8757],[30,49,4730],[29,35,1055],[42,48,3879],[41,66,7190],[8,92,553],[47,43,9649],[64,24,1713],[69,2,7953],[15,69,5088],[26,43,8658],[81,79,5528],[63,83,2226],[16,2,2636],[3,33,4023],[22,64,9274],[84,65,5072],[28,83,4374],[37,20,3426],[92,2,6569],[60,49,8330],[63,84,4727],[25,23,7348],[51,31,849],[87,5,8395],[14,65,4064],[44,42,1357],[69,46,2152],[62,82,315],[45,27,8891],[64,21,7901],[31,38,6426],[4,43,6567],[9,75,3267],[80,45,8804],[67,56,9315],[51,27,707],[12,29,7760],[82,1,8974],[55,56,2774],[56,8,3386],[18,60,1791],[55,39,90],[27,7,381],[89,8,1908],[27,5,8103],[65,15,2437],[85,54,5325],[88,14,4987],[73,57,4029],[78,43,9335],[33,14,6606],[1,53,5848],[61,24,4545],[87,30,2518],[66,21,1389],[74,23,3923],[27,75,1732],[51,52,1517],[25,7,1083],[65,47,4406],[83,27,2801],[38,16,7112],[93,6,7713],[37,52,1730],[0,74,1208],[51,3,8052],[88,66,9789],[16,1,9038],[0,56,2083],[57,47,7505],[64,62,9096],[71,62,9691],[79,8,3248],[64,83,9087],[7,33,2412],[8,12,2670],[33,87,4170],[18,72,2504],[48,4,9277],[41,12,7898],[74,24,7647],[32,11,6244],[88,33,8534],[51,30,9628],[3,60,2769],[40,48,1788],[73,48,2312],[90,38,9022],[26,3,9624],[43,77,5959],[25,29,6696],[88,83,308],[70,79,8023],[80,49,724],[33,64,5651],[40,57,467],[58,30,6167],[56,87,113],[59,90,9502],[92,39,6346],[63,24,4863],[1,77,5365],[60,74,8050],[89,35,3818],[8,71,2879],[50,53,1678],[19,47,2113],[7,31,5908],[20,40,314],[52,73,5193],[44,49,9837],[84,18,3288],[65,6,658],[19,3,9631],[38,68,7404],[3,20,7230],[17,74,6058],[23,89,7254],[58,71,5114],[63,7,4550],[12,76,4233],[63,47,7120],[62,72,300],[10,71,3311],[75,9,7364],[0,71,6546],[52,69,2155],[3,54,4344],[46,15,6383],[37,57,1168],[22,7,5221],[88,72,912],[73,69,2786],[8,51,3247],[58,22,2742],[0,11,6114],[53,69,4490],[50,39,3003],[12,33,2108],[81,89,2867],[85,49,9411],[87,44,2009],[34,32,6507],[74,42,7627],[37,82,3649],[26,9,4455],[45,44,5561],[9,22,4970],[16,89,5259],[77,78,5784],[26,4,2884],[12,8,9625],[62,88,7187],[4,26,5493],[2,47,7647],[60,70,5098],[11,71,547],[62,93,4399],[20,19,7799],[52,33,8168],[76,19,537],[10,50,6748],[27,49,768],[3,41,7941],[0,22,9822],[71,86,2089],[19,21,5944],[91,86,4143],[38,21,8735],[78,10,8301],[68,11,6229],[50,8,4610],[37,38,8598],[54,42,7578],[51,64,2508],[86,45,237],[45,75,9814],[2,36,5135],[3,30,5866],[39,70,2875],[38,14,3136],[21,49,2043],[46,43,3941],[40,25,7039],[15,54,6715],[13,24,2912],[52,83,3170],[4,50,659],[58,36,8108],[63,13,9259],[49,40,8124],[64,55,273],[65,4,7479],[87,57,3524],[58,34,8859],[75,18,8377],[36,87,8610],[20,27,9776],[16,13,9341],[10,27,760],[82,24,8645],[36,43,8610],[42,38,9556],[66,23,7624],[45,52,4753],[1,33,5291],[2,48,6593],[23,16,7302],[35,18,8002],[74,45,1588],[42,54,7207],[67,2,9109],[33,21,8171],[26,12,2537],[45,30,673],[83,14,1728],[35,27,3044],[5,83,4017],[85,87,8963],[82,28,301],[66,64,4095],[6,35,4026],[23,17,5777],[18,51,4196],[92,8,7656],[65,87,4216],[1,79,7912],[74,2,6267],[90,81,3508],[21,14,4249],[44,43,5725],[20,41,1208],[33,74,7521],[90,51,8738],[53,64,4793],[72,90,1285],[24,56,7374],[55,76,1744],[7,60,8365],[90,71,5512],[24,38,2166],[66,46,2775],[39,65,5803],[81,92,9938],[15,67,1807],[87,65,7414],[25,83,9961],[39,1,5150],[93,26,6700],[83,13,4395],[93,49,751],[41,76,673],[80,92,1673],[16,33,5972],[29,61,9336],[78,46,4588],[18,21,2264],[5,62,9366],[48,68,9341],[27,51,1274],[93,89,5036],[78,50,5148],[35,30,54],[63,38,8301],[2,50,7308],[12,79,8809],[7,35,5468],[11,26,4662],[10,48,4802],[28,35,379],[85,42,1906],[38,13,2249],[40,89,1341],[77,44,1973],[53,90,7130],[14,80,8854],[57,37,2766],[2,18,1042],[57,34,1160],[74,67,6054],[69,48,8610],[0,53,8921],[73,3,8043],[89,72,9300],[59,91,7242],[80,50,8127],[89,29,7655],[54,75,2950],[17,48,6840],[19,36,913],[2,79,5808],[75,32,9283],[67,59,6412],[69,93,7165],[56,62,1504],[62,28,5821],[4,78,5810],[70,32,1099],[78,13,9415],[70,6,7961],[41,14,3517],[21,8,3657],[52,25,1723],[75,23,4537],[85,27,4356],[3,51,9107],[77,68,2816],[46,78,2045],[24,53,4164],[70,68,6960],[21,52,2694],[72,91,606],[22,12,4956],[26,84,6320],[90,70,5498],[63,50,7550],[78,40,1487],[51,63,1554],[2,20,4423],[74,92,5199],[3,26,4642],[53,86,9947],[4,72,3520],[84,86,7490],[1,50,5091],[27,88,5200],[16,32,4670],[88,54,4346],[42,11,2451],[92,78,8621],[74,54,9836],[88,53,4446],[0,67,2647],[87,84,639],[15,13,2807],[3,48,2994],[41,49,430],[52,37,2595],[39,48,6070],[23,72,2588],[33,70,6716],[6,56,7267],[49,59,6089],[43,21,5835],[44,65,8120],[35,19,8353],[41,47,2442],[46,72,5934],[6,18,5003],[71,45,6940],[67,47,4888],[56,63,2616],[56,43,6748],[30,12,6315],[19,33,1186],[36,8,445],[23,88,3896],[84,25,2666],[7,32,2739],[18,10,6390],[65,83,9723],[93,87,8918],[18,22,7153],[34,85,7387],[85,33,3394],[55,25,2599],[15,26,6780],[50,74,6532],[53,6,1606],[0,78,4997],[0,39,4734],[39,30,9025],[60,65,2906],[12,83,7377],[54,80,6620],[5,78,5205],[3,65,714],[16,43,843],[61,93,5698],[2,86,2978],[50,84,8921],[50,35,9890],[90,69,9280],[35,4,8916],[83,58,4646],[42,7,5297],[52,1,9112],[23,25,9824],[0,77,6959],[74,81,2769],[55,93,5563],[11,64,2778],[6,80,2678],[45,65,3190],[21,34,1865],[80,85,957],[14,84,6689],[33,39,8526],[61,83,5653],[39,80,886],[71,46,2163],[56,90,198],[51,71,7391],[5,32,9711],[17,65,1190],[0,40,5444],[23,29,5921],[74,64,6057],[70,49,8438],[5,10,3794],[60,34,9644],[27,79,2861],[90,88,4359],[4,20,368],[73,61,7428],[49,43,4778],[7,45,6125],[78,57,1580],[86,51,2365],[86,29,8095],[43,63,3160],[61,15,6609],[51,23,6164],[1,20,3715],[32,92,1412],[40,20,8229],[78,23,7756],[12,90,7418],[52,39,8982],[70,85,6743],[60,41,7375],[35,51,7945],[68,71,3946],[15,25,6124],[2,51,6902],[87,12,3333],[9,12,5224],[31,42,7068],[54,45,7741],[24,76,7450],[31,59,4084],[64,73,4260],[55,29,9920],[68,13,6959],[49,72,1197],[27,83,7497],[64,44,999],[8,70,9264],[78,52,1177],[41,91,7343],[67,8,2123],[91,92,1941],[53,16,4373],[19,30,5724],[93,67,9204],[42,29,2101],[81,83,4581],[66,33,1892],[88,39,3996],[79,46,3219],[70,30,9834],[43,69,4561],[27,6,7944],[20,46,10000],[55,35,9868],[91,36,905],[63,76,2974],[67,72,2442],[37,74,4050],[45,63,630],[83,36,3210],[81,3,8717],[50,81,4333],[84,36,960],[80,83,8723],[53,24,5243],[79,49,1769],[59,70,4252],[91,11,4978],[29,52,5974],[19,35,1195],[48,62,9219],[16,36,4824],[72,82,9072],[90,63,5063],[70,57,7495],[20,8,5899],[47,54,3611],[32,27,2800],[63,0,7330],[72,32,3223],[29,67,9742],[56,34,5109],[47,91,5431],[30,56,237],[48,44,2375],[64,31,1729],[36,58,9586],[27,90,8399],[39,78,3192],[4,69,4427],[10,26,2343],[6,61,5088],[68,43,6502],[81,34,5263],[92,21,2227],[44,61,5403],[19,22,8932],[49,38,7182],[64,69,932],[34,58,7137],[6,53,2871],[73,90,122],[35,79,2453],[70,75,2314],[88,9,2508],[16,87,9541],[48,72,9884],[91,63,5309],[51,14,840],[11,61,940],[38,60,9519],[20,31,6616],[57,87,2866],[42,64,5913],[87,51,7358],[54,60,3260],[28,92,5131],[61,3,7648],[15,16,6587],[79,59,3572],[76,16,326],[63,41,7590],[9,66,2522],[30,93,5764],[65,58,4562],[79,76,5510],[61,64,5947],[56,93,9623],[54,89,8514],[82,37,8473],[66,41,112],[21,51,310],[71,36,1723],[57,27,5036],[90,24,872],[29,1,7896],[49,51,998],[25,46,1925],[59,92,6427],[44,31,9463],[57,13,1362],[1,69,6154],[27,84,2003],[55,68,6116],[11,9,2015],[21,43,6417],[50,80,7801],[73,23,6819],[23,45,2212],[6,4,4348],[49,16,6310],[14,3,5754],[36,61,7295],[46,32,536],[80,7,5707],[28,31,7213],[77,74,3766],[86,71,4069],[31,62,3028],[18,92,8360],[82,61,5232],[39,88,7310],[78,60,1245],[92,84,6639],[78,48,970],[21,48,1821],[52,85,3339],[30,66,8754],[81,72,6556],[63,59,1402],[56,58,4899],[19,13,6200],[16,49,1617],[85,80,4851],[73,14,7049],[55,45,4616],[35,73,9412],[22,61,572],[16,31,7019],[76,92,6840],[84,6,8655],[1,87,3948],[54,29,9980],[62,31,3644],[56,21,2247],[65,62,1930],[20,91,2641],[52,66,1708],[90,9,4640],[16,10,4031],[67,53,5872],[87,26,6107],[8,68,9026],[65,72,4031],[56,26,3878],[93,12,506],[52,75,27],[8,67,4078],[83,38,4359],[40,71,8752],[0,46,5647],[27,72,1128],[85,2,7435],[17,13,948],[55,83,5075],[80,27,8852],[6,8,8150],[81,78,738],[5,82,1680],[25,90,3561],[7,15,9166],[34,15,8668],[89,62,1825],[72,70,9467],[84,28,9894],[78,36,812],[71,37,8896],[6,28,3420],[5,65,3546],[57,81,3757],[71,39,6024],[58,8,4943],[56,23,2288],[4,57,9587],[9,28,408],[16,44,4266],[85,52,7421],[9,50,4514],[91,26,5106],[43,19,5496],[24,78,5682],[79,74,8944],[22,93,2902],[51,28,173],[48,91,7388],[85,24,6185],[19,85,5583],[40,90,4185],[0,3,1456],[76,38,2922],[93,73,8263],[29,10,8413],[46,68,4915],[37,15,1255],[49,83,4835],[34,66,6173],[51,82,7649],[90,30,5211],[1,32,5606],[73,8,6138],[67,23,8083],[75,46,5734],[71,13,6124],[0,34,4322],[44,39,1041],[90,18,6885],[23,31,6397],[74,82,7923],[22,42,3816],[89,92,8377],[61,87,5515],[44,7,7167],[57,48,168],[70,7,5224],[21,50,9769],[73,86,5505],[57,56,7556],[64,1,280],[29,28,1647],[68,59,6244],[27,87,5883],[36,31,1370],[6,91,4940],[67,74,4108],[71,91,5209],[85,6,3303],[61,84,3202],[75,16,9191],[58,35,2894],[13,28,5018],[4,85,3850],[84,12,5755],[78,18,7043],[1,92,5456],[60,57,2000],[76,80,6229],[24,42,1282],[66,65,9213],[42,93,7182],[57,29,1099],[10,57,6410],[17,21,2012],[90,82,6593],[13,36,7167],[90,56,5006],[14,10,7952],[2,85,6095],[60,26,7980],[88,49,5012],[69,64,8271],[85,38,8081],[71,26,3862],[16,47,8673],[1,72,4096],[25,58,6982],[60,82,5166],[75,66,4935],[75,54,140],[42,6,4591],[34,30,1281],[74,1,5006],[5,66,4016],[75,10,3825],[8,57,3418],[23,53,2047],[25,40,7288],[29,44,4683],[32,73,2872],[59,52,462],[49,29,1372],[5,37,9517],[63,72,4557],[86,54,327],[63,51,6437],[0,29,8132],[76,63,5665],[93,54,4012],[40,0,2505],[14,34,3153],[64,3,8317],[52,5,7738],[6,71,7633],[10,67,5916],[15,6,2570],[30,69,2834],[60,77,85],[13,35,7604],[36,67,8573],[42,23,8295],[37,7,1717],[50,28,2645],[68,55,7311],[62,15,3523],[90,85,5186],[72,46,1149],[62,11,2867],[84,88,4616],[43,2,392],[68,29,8052],[1,28,8272],[15,77,8658],[74,87,7758],[88,78,8660],[53,21,6239],[57,24,1986],[76,61,9028],[58,56,7133],[47,17,4564],[3,72,6617],[30,70,8303],[5,26,3359],[27,76,2571],[50,89,7444],[29,25,6135],[58,32,969],[69,70,7159],[48,30,3620],[8,83,7189],[69,74,9912],[25,81,5882],[30,79,3015],[89,21,5492],[40,79,8776],[45,36,4955],[13,84,1220],[77,26,7715],[57,3,6788],[14,27,2766],[79,35,6421],[18,0,8247],[1,66,3714],[54,16,5236],[17,37,253],[63,2,3868],[54,10,835],[26,55,1952],[59,24,2728],[92,53,3674],[37,67,6154],[1,74,938],[83,20,1774],[5,41,369],[17,59,484],[33,20,9644],[49,52,5576],[12,25,278],[69,78,297],[3,47,4108],[77,47,1612],[49,22,132],[60,13,1781],[17,0,6476],[62,7,6317],[57,36,1735],[71,44,4328],[25,68,5435],[52,89,5626],[43,41,8753],[25,88,6654],[81,24,474],[20,32,2577],[38,70,2285],[90,57,9023],[9,48,3893],[37,63,4758],[59,71,2737],[36,3,105],[86,10,4911],[25,28,2204],[12,71,8798],[1,18,4980],[77,57,1682],[79,33,6247],[16,20,69],[33,88,1960],[49,86,25],[39,23,8837],[34,25,9168],[68,93,8149],[30,85,1981],[93,38,7027],[52,3,5543],[45,24,3731],[77,55,255],[65,57,7870],[34,53,6654],[52,92,1881],[32,61,2890],[14,93,2155],[54,59,5000],[82,77,3106],[81,69,8087],[39,42,5784],[23,12,4665],[87,61,9923],[55,4,9841],[55,82,2844],[57,17,2629],[21,1,9172],[29,80,1370],[5,80,6875],[92,87,8364],[56,60,2322],[1,65,1765],[22,58,8340],[41,61,767],[4,49,9842],[10,12,7788],[62,23,7413],[14,41,4986],[51,39,316],[27,34,4789],[58,73,7240],[18,64,1389],[21,60,5490],[73,88,3236],[38,88,9265],[21,13,9251],[35,49,5304],[86,20,5225],[5,40,8534],[75,8,1754],[55,37,2116],[53,88,5769],[12,1,1085],[82,80,5290],[65,30,7030],[47,29,2674],[23,35,8289],[3,87,730],[39,28,9682],[78,54,1266],[58,68,8521],[90,2,2370],[60,11,5684],[24,2,7620],[39,52,5991],[34,82,2692],[59,20,1524],[78,61,28],[78,16,1545],[79,10,9410],[47,4,9732],[71,33,2724],[29,11,974],[42,31,5908],[73,80,4469],[35,92,3350],[73,83,6597],[22,38,1961],[55,26,8264],[59,67,5066],[5,11,5046],[91,17,7596],[29,8,5137],[89,13,8791],[64,4,4895],[52,46,6165],[34,63,863],[80,24,7488],[48,21,5395],[86,7,7339],[78,49,9325],[59,78,1181],[72,36,6343],[47,92,6828],[72,35,4672],[3,15,3990],[45,22,3449],[66,93,7198],[42,52,9710],[63,58,7711],[55,67,2965],[44,11,3182],[27,70,2974],[7,73,2721],[25,47,5426],[40,76,1253],[7,0,6204],[0,8,2726],[86,57,1890],[66,15,7554],[46,0,9238],[78,66,9356],[75,12,3648],[48,64,955],[60,66,3670],[13,73,9577],[72,6,8148],[67,22,6681],[48,34,4811],[88,65,570],[3,6,4722],[43,58,3454],[32,22,3812],[34,33,1039],[45,33,9540],[63,17,7092],[90,15,9492],[73,70,5023],[26,59,195],[4,60,9276],[31,9,5658],[40,32,7788],[1,90,2336],[39,56,8938],[43,32,9758],[50,16,6283],[49,78,7345],[24,71,6162],[11,41,5185],[27,28,5729],[85,35,1271],[50,78,7534],[73,36,3462],[14,40,2187],[71,61,5672],[13,2,7180],[28,43,7590],[88,17,8338],[6,78,3969],[90,66,7403],[10,38,1528],[63,73,1752],[67,1,7263],[5,86,4624],[41,55,864],[32,81,2519],[7,8,5584],[12,64,3899],[31,64,8262],[70,66,3801],[23,13,9879],[55,12,8096],[38,46,1203],[6,7,2233],[5,34,8862],[25,64,3693],[48,59,2550],[91,85,2475],[37,50,3266],[93,57,6787],[24,7,8017],[18,34,2338],[34,3,4784],[90,13,477],[62,4,1124],[69,38,2405],[79,81,4880],[60,1,4459],[52,35,7952],[1,46,5088],[75,26,6004],[42,1,8578],[30,87,6339],[38,72,5083],[35,12,4241],[58,46,2386],[7,11,1696],[54,35,4485],[63,29,1237],[58,88,7452],[6,19,6530],[51,33,1309],[17,30,8354],[90,3,7996],[47,19,7542],[77,13,3194],[43,24,9375],[83,1,411],[87,58,256],[26,52,1943],[91,59,2069],[74,59,2328],[39,87,6488],[33,27,1147],[37,18,4083],[24,19,7664],[60,64,5471],[37,66,1710],[11,8,4387],[52,90,2742],[27,21,7541],[14,20,9965],[61,52,5955],[50,48,9520],[56,10,5451],[47,75,2390],[11,22,5360],[55,63,1967],[84,45,2601],[39,81,1939],[80,56,6972],[19,65,1604],[68,92,5545],[47,68,8931],[38,7,1685],[37,27,9845],[5,22,8444],[51,29,9067],[67,68,4109],[42,41,6981],[56,52,9992],[8,49,9085],[56,64,1629],[69,65,9177],[37,48,6443],[19,24,6061],[86,64,322],[73,31,5793],[41,0,4428],[52,19,8174],[55,90,9625],[46,2,355],[21,90,6486],[28,59,6931],[16,27,424],[70,92,8558],[67,17,5592],[28,80,6407],[86,21,2677],[6,31,4031],[4,81,3444],[32,71,4639],[1,59,9673],[81,64,4235],[9,16,587],[89,79,2641],[83,85,5442],[38,91,3096],[40,81,4221],[32,65,1404],[37,8,1411],[20,58,6654],[78,35,3746],[10,16,7410],[61,29,5470],[0,6,4218],[22,35,8256],[81,36,5237],[21,77,8944],[33,7,6091],[3,14,1110],[0,15,7704],[70,71,1655],[1,8,6413],[24,1,8259],[82,88,3218],[27,64,9867],[49,26,1113],[68,37,4264],[39,58,8578],[82,7,9168],[43,22,830],[74,60,3829],[84,59,6926],[84,67,1311],[71,64,2976],[11,0,9915],[66,9,6380],[86,41,2928],[82,4,4906],[11,43,289],[87,31,3120],[68,72,7704],[62,66,381],[82,72,9054],[54,46,6437],[74,58,995],[64,51,1676],[8,19,2971],[87,0,1439],[79,24,4648],[6,45,472],[38,53,4174],[76,45,35],[65,89,4054],[9,92,8352],[70,80,133],[17,28,6264],[51,16,7995],[40,38,9772],[33,78,7435],[57,80,6439],[33,40,8403],[44,76,8526],[87,70,9641],[24,73,3008],[82,74,2162],[11,66,4049],[49,57,9718],[59,4,7335],[78,56,6005],[23,18,7553],[23,81,1264],[42,86,763],[72,12,4230],[10,54,8271],[7,58,2088],[73,40,4682],[12,37,546],[21,72,4219],[37,84,1121],[23,26,5435],[25,62,4027],[78,64,7043],[60,63,6537],[2,33,3017],[45,49,9147],[35,91,8054],[89,5,5824],[13,62,520],[9,35,6088],[59,14,6258],[29,6,9552],[57,67,3806],[23,22,7867],[73,27,5800],[93,29,1041],[67,30,5570],[86,76,9764],[90,25,585],[75,3,3301],[61,60,1009],[7,5,7611],[35,36,6585],[43,0,1451],[2,59,9310],[57,44,9231],[58,86,9451],[74,35,4369],[62,81,4397],[39,36,7064],[69,6,4875],[43,81,66],[52,6,8007],[26,62,3827],[39,55,5688],[76,9,2311],[54,40,3102],[51,86,4674],[61,13,251],[1,86,245],[9,56,5962],[90,32,1903],[51,24,4305],[62,6,1980],[1,34,9933],[21,40,3362],[91,12,8140],[35,45,7569],[72,69,9832],[59,11,8292],[81,60,7620],[79,32,3013],[15,11,521],[78,20,4966],[49,42,5701],[84,22,2866],[60,90,5807],[36,92,8881],[28,71,6882],[84,20,46],[21,2,4603],[17,22,245],[89,76,6810],[88,31,5878],[77,6,8653],[35,28,521],[24,68,4954],[13,63,9700],[16,26,9492],[58,89,5343],[30,32,3867],[39,20,8523],[88,48,9804],[11,79,6185],[92,27,6529],[91,5,5508],[85,55,2958],[77,37,6818],[37,69,3694],[54,11,6559],[6,10,1738],[72,75,5813],[88,12,4526],[81,91,9937],[81,4,6094],[72,24,3727],[50,21,8258],[62,78,4796],[88,5,7653],[50,4,7719],[28,22,6466],[23,20,4005],[71,2,7621],[25,17,5972],[57,70,8875],[5,84,1977],[46,65,3770],[49,7,558],[0,55,4934],[3,90,8391],[45,87,215],[11,57,7436],[37,19,1434],[70,1,202],[78,39,9144],[53,73,6795],[3,49,3584],[89,30,1060],[93,17,5857],[45,64,1571],[2,74,5028],[86,62,8009],[84,77,2354],[21,29,9080],[82,25,9948],[27,46,7975],[7,22,2487],[61,90,6241],[51,78,5593],[50,11,5960],[54,79,3008],[83,63,6301],[69,85,3699],[7,42,7188],[13,32,9012],[17,67,4766],[30,90,1333],[35,93,3315],[58,84,3793],[37,25,1664],[57,60,8174],[30,1,5275],[33,54,9200],[72,52,2892],[11,56,2715],[62,92,9861],[20,10,9016],[15,86,4478],[56,1,2045],[21,35,1294],[70,37,8399],[78,44,2677],[11,74,4778],[37,80,3274],[21,54,4161],[4,34,3468],[84,19,6762],[57,11,1686],[63,81,2404],[83,30,1707],[66,62,706],[91,70,4106],[31,87,2604],[18,83,7336],[80,42,7755],[68,27,4605],[20,11,8579],[20,50,8906],[75,60,4314],[93,27,4478],[57,66,6446],[68,57,1805],[74,78,9758],[0,64,178],[68,53,7991],[43,44,5042],[31,73,5581],[75,19,2624],[87,46,1569],[0,42,2109],[21,88,5688],[25,9,379],[79,60,5839],[0,52,9040],[86,17,3845],[5,81,7361],[20,3,757],[50,71,5073],[14,30,4428],[3,5,6324],[2,38,6096],[28,45,3346],[56,19,8790],[88,0,8231],[12,44,1719],[1,17,415],[9,49,7185],[11,48,3978],[80,51,1386],[5,21,6499],[36,33,275],[30,34,9617],[5,13,8334],[49,92,4475],[40,41,5809],[25,39,8184],[45,25,9168],[75,39,5231],[36,38,2094],[85,66,3317],[30,16,8811],[70,11,6008],[41,21,1278],[88,24,6309],[20,37,5659],[15,43,5533],[61,66,113],[29,57,9113],[20,22,6491],[2,83,2746],[74,7,1413],[11,28,8306],[40,61,3773],[53,56,1707],[56,6,6232],[35,21,3972],[2,55,208],[13,37,3351],[9,34,5765],[79,21,9696],[53,1,1281],[1,60,6470],[43,10,4496],[54,8,4039],[80,36,596],[77,28,6534],[45,82,7890],[84,43,7153],[17,53,6624],[38,63,2848],[11,65,6496],[61,85,92],[68,18,2579],[36,23,9319],[69,3,8275],[33,5,5001],[63,79,4473],[9,3,1359],[32,86,7500],[11,16,6465],[39,10,232],[91,31,466],[71,93,2983],[66,30,2466],[89,57,2977],[54,24,5623],[79,5,301],[44,74,1613],[65,37,24],[52,62,9318],[75,5,2519],[29,39,8076],[35,15,6376],[26,91,4590],[45,5,5733],[75,33,1647],[43,80,7859],[20,0,7131],[34,59,8995],[72,20,5364],[65,52,7882],[42,69,9332],[13,88,8455],[92,66,5832],[78,24,2368],[22,50,5301],[50,59,1478],[48,15,8466],[22,57,7933],[70,76,6886],[75,37,4128],[24,5,6771],[42,87,2646],[17,52,2951],[36,76,99],[84,83,8395],[38,5,2641],[83,65,4606],[2,34,7010],[3,2,9980],[49,76,8406],[17,16,3110],[15,45,7371],[67,9,9675],[57,6,6341],[70,58,5600],[72,11,8154],[35,55,9504],[78,72,8467],[43,29,1337],[53,62,3506],[71,82,6952],[77,86,1886],[65,35,1951],[76,32,1263],[45,73,7694],[21,64,6236],[5,17,7789],[49,80,7384],[21,39,8735],[20,21,5045],[62,74,952],[48,89,9023],[4,41,5718],[39,47,3820],[59,49,3741],[84,5,8114],[52,43,3005],[2,57,9201],[81,70,3122],[80,89,4738],[26,90,4747],[34,62,3902],[32,45,8186],[80,22,9786],[42,75,8755],[20,71,2885],[44,30,6180],[24,25,5790],[69,4,7173],[77,3,5624],[61,17,752],[86,81,9673],[7,63,4061],[71,40,8031],[72,38,5455],[50,90,517],[6,30,6591],[93,86,9514],[7,26,8933],[18,85,4717],[33,8,8918],[84,76,2237],[74,17,123],[59,13,9327],[69,19,6725],[85,23,1890],[66,34,6789],[23,92,2296],[90,7,6587],[29,15,6561],[5,4,8093],[37,58,7839],[92,76,5589],[65,63,1313],[65,1,3776],[2,1,1925],[40,69,3336],[92,46,6110],[51,4,644],[0,12,2936],[35,33,2727],[67,46,4403],[32,8,5325],[54,38,666],[66,38,2324],[82,68,9201],[51,68,9852],[80,75,385],[9,46,2290],[62,18,7505],[50,85,802],[84,47,6939],[59,35,2097],[39,83,6365],[3,59,1022],[84,31,9250],[10,33,357],[26,33,7716],[92,17,319],[81,9,3743],[87,49,1755],[39,79,6242],[25,65,196],[60,0,2377],[1,54,7283],[73,35,2650],[74,83,2819],[15,49,4738],[71,11,5375],[9,39,5016],[19,60,6030],[39,57,2868],[77,83,4147],[89,91,9458],[89,63,5981],[81,42,4273],[55,72,9384],[50,12,5787],[76,6,423],[77,20,4424],[29,31,9628],[5,51,2472],[53,50,6319],[52,21,6193],[16,82,3841],[92,7,4684],[64,78,369],[6,63,1583],[84,10,8224],[66,19,9093],[54,2,5307],[61,54,1947],[17,6,3353],[77,53,286],[80,48,4671],[75,28,9997],[49,75,8654],[70,12,6706],[18,43,1675],[48,26,5738],[25,82,7959]]
# print(len(flights))
src = 17
dst = 33
k = 39
print(s.findCheapestPrice(n, flights, src, dst, k) == 1502) 


n = 19
flights = [[3,15,7066],[2,7,9254],[15,12,54],[6,8,8137],[7,12,9819],[5,2,7956],[14,3,6675],[8,14,4543],[5,13,1689],[2,12,1220],[9,15,5710],[11,13,5799],[16,3,154],[4,6,5499],[13,2,1143],[0,6,485],[16,2,5211],[9,7,4453],[0,8,8798],[4,9,4760],[16,6,9182],[6,18,3774],[17,3,630],[0,2,5689],[18,1,4688],[4,11,4044],[14,0,4253],[2,18,3697],[16,18,7525],[15,14,1480],[2,10,4931],[10,8,1741],[3,10,7964],[7,15,7880],[17,2,9694],[6,14,9167],[10,1,6844],[13,3,4742],[16,15,6428],[0,1,5819],[13,17,2815],[14,17,5654],[5,3,8906],[9,14,9342],[7,17,3559],[16,12,2633],[17,9,331],[10,4,3234],[2,17,9607],[12,5,2003],[5,9,6784],[15,0,175],[10,11,6834],[2,9,6348],[18,13,7372],[15,7,3535],[1,14,7877],[1,4,8036],[7,16,7089],[1,12,6523],[4,14,3668],[1,10,8785],[1,13,1219],[13,11,8834],[18,11,2920],[12,2,531],[4,17,8509],[2,11,3368],[16,5,5302],[14,5,6143],[10,14,1639],[10,16,7114],[10,13,9941],[13,18,1779],[9,5,5628],[12,14,2892],[11,17,1064],[1,17,8652],[15,16,8192],[9,10,260],[7,1,6405],[16,7,3532],[3,0,9842],[12,16,3233],[13,1,8375],[10,7,6730],[18,4,6232],[17,5,7097],[14,13,7290],[10,2,4442],[13,5,8228],[14,6,4709],[6,11,4636],[14,8,10000],[8,9,9133],[5,18,6091],[10,3,6397],[4,3,8425],[14,12,7883],[4,16,901],[16,4,4051],[1,0,7827],[5,11,8596],[18,9,4058],[18,6,5500],[16,9,2414],[12,11,4230],[1,6,3821],[18,0,1299],[11,5,4232],[15,2,5251],[12,13,1716],[17,15,3],[0,16,1708],[3,11,661],[17,16,9213],[8,0,2913],[2,6,556],[5,1,9106],[16,10,7006],[2,13,3038]]
src = 12
dst = 10
k = 0
print(s.findCheapestPrice(n, flights, src, dst, k) == -1) 


n = 7
flights = [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]]
src = 2
dst = 4
k = 1
print(s.findCheapestPrice(n, flights, src, dst, k) == 16) 

# for f in flights:
#     print(f[0], f[1], f[2])
# n = 8
# flights = [[0,1,28],[1,2,39],[2,3,59],[3,0,7],
#            [1,4,38],
#            [4,5,35],[5,6,23],[6,7,26],[7,4,65],
#            [7,2,15]]
# src = 0
# dst = 7
# k = 13
# print(s.findCheapestPrice(n, flights, src, dst, k)) #TLE

# stack = [iter({1:None, 2:None, 3:None})]

# children = stack[-1]
# print(set(children))
# print(set(children))

# while stack:
#     children = stack[-1]
#     child = next(children, None)
#     if child in {1:None}:
#         continue
#     if child is None:
#         stack.pop()
#     print(child)

# print(set() - {1,2})
# print({1}.add(1))