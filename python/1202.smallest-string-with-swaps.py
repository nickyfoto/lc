#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#
# https://leetcode.com/problems/smallest-string-with-swaps/description/
#
# algorithms
# Medium (39.16%)
# Total Accepted:    4.1K
# Total Submissions: 10.6K
# Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
#
# You are given a string s, and an array of pairs of indices in the string
# pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# 
# You can swap the characters at any pair of indices in the given pairs any
# number of times.
# 
# Return the lexicographically smallest string that s can be changed to after
# using the swaps.
# 
# 
# Example 1:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# 
# 
# Example 2:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# 
# Example 3:
# 
# 
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
# 
# 
#
from collections import defaultdict


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

class Solution:
    # def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    def smallestStringWithSwaps(self, s, pairs) -> str:

        # d = Counter(map(tuple, pairs))
        n = len(s)
        # import networkx as nx
        # g = nx.Graph()
        g = Graph()
        g.add_nodes_from(range(n))
        g.add_edges_from(pairs)

        

        explored = defaultdict(lambda: False)

        def cc(g):
            num_cc = 0
            # arr = [0] * len(g)
            arr = defaultdict(list)

            def dfs(node, num_cc):
                arr[num_cc].append(node)
                explored[node] = True
                for neighbor in g.neighbors(node):
                    if not explored[neighbor]:
                        dfs(neighbor, num_cc)

            for node in g:
                if not explored[node]:
                    dfs(node, num_cc)
                    num_cc += 1

            return arr, num_cc

        cc, num_cc = cc(g)

        # print(cc, num_cc)

        # if num_cc == 1:
            # return "".join(sorted(list(s))) 


        # else:
        s = list(s)
        c = s.copy()
        for nodes in cc.values():
            # nodes = [idx for idx in range(n) if cc[idx] == i]
            # print(nodes)
            indices = sorted(nodes, key=lambda x: s[x])
            # print(indices)
            nodes.sort()
            for j in range(len(nodes)):
                # print(nodes[j], indices[j])

                s[nodes[j]] = c[indices[j]]
        # print(s)
        return "".join(s)





        
