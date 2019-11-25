#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/



# from coreviews import AdjacencyView
# from reportviews import NodeView
from collections.abc import Mapping, Set

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
            return iter(self._adj[n])
        except KeyError:
            raise NetworkXError("The node %s is not in the graph." % (n,))

    def is_directed(self):
        """Returns True if graph is directed, False otherwise."""
        return False

    def is_multigraph(self):
        """Returns True if graph is a multigraph, False otherwise."""
        return False




# import networkx as nx
from itertools import combinations
from collections import defaultdict
# from graph import Graph

class Solution:
    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    def accountsMerge(self, accounts):

        n = len(accounts)


        class Account:
            def __init__(self, account, idx):
                self.name = account[0]
                self.emails = set(account[1:])
                self.num_of_emails = len(self.emails)
                self.idx = idx
        accounts.sort()
        accounts = list(Account(x,y) for x,y in zip(accounts, range(n)))

        i = 0

        merged = []


        def connected_components(g):

            def dfs(node):
                cc[num_of_cc].append(node)
                explored[node] = True
                for neighbor in g.neighbors(node):
                    if not explored[neighbor]:
                        dfs(neighbor)

            num_of_cc = 1
            cc = defaultdict(list)
            explored = defaultdict(lambda: False)
            for node in g.nodes:
                if not explored[node]:
                    dfs(node)
                    num_of_cc += 1
            # print(cc)
            # print(cc.values())
            return num_of_cc - 1, cc.values()

        while i < n:
            name = accounts[i].name
            same_name = [accounts[i]]
            i += 1
            while i < n and accounts[i].name == name:
                same_name.append(accounts[i])
                i += 1
            # same_name_list.append(same_name)
            if len(same_name) > 1:
                # print(len(same_name))
                email_sets = [n.emails for n in same_name]
                # print(email_sets)
                # g = nx.Graph()
                g = Graph()
                for emails in email_sets:
                    if len(emails) == 1:
                        g.add_node(list(emails)[0])
                    else:
                        g.add_edges_from(combinations(emails, r=2))

                num_of_cc, cc = connected_components(g)

                for c in cc:
                    merged.append([name] + sorted(list(c)))
            else:
                # print(same_name)
                merged.append([name] + sorted(list(same_name[0].emails)))
        # print(merged)
        return merged


# s = Solution()


# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

# print(s.accountsMerge(accounts))


# accounts = [["David","David5@m.co","David8@m.co"],["David","David1@m.co","David1@m.co","David8@m.co"],["David","David0@m.co","David0@m.co","David5@m.co"]]




# expected = [["David","David0@m.co","David1@m.co","David5@m.co","David8@m.co"]]



# my_op = [["David","David0@m.co","David5@m.co"],["David","David1@m.co","David5@m.co","David8@m.co"]]



# accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]

# expected = [["Alex","Alex0@m.co","Alex4@m.co","Alex5@m.co"],["Ethan","Ethan0@m.co","Ethan3@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],["Kevin","Kevin2@m.co","Kevin4@m.co"]]




# my_op = [["Ethan","Ethan0@m.co","Ethan3@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],["Gabe","Gabe0@m.co","Gabe2@m.co","Gabe3@m.co","Gabe4@m.co"],["Kevin","Kevin2@m.co","Kevin4@m.co"]]


# print(sorted(my_op))


# accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# expected = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# my_op =    [["John","johnnybravo@mail.com"],["John","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"]]





















