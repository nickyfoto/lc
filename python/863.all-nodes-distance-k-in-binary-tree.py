#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (49.99%)
# Total Accepted:    32.9K
# Total Submissions: 65.8K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# We are given a binary tree (with root node root), a target node, and an
# integer value K.
# 
# Return a list of the values of all nodes that have a distance K from the
# target node.  The answer can be returned in any order.
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
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 
# Output: [7,4,1]
# 
# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
# 
# 
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these
# objects.
# 
# 
# 
# 
# Note:
# 
# 
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Graph:
    def __init__(self):
        self._node = {}
        self._adj = {}

    @property
    def adj(self):
        return self._adj

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

class Solution:
    def distanceK2(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if K == 0:
            return [target.val]

        # get target_level
        q = [[root]]
        level = 0
        while q:
            nodes = q.pop(0)
            l = []
            for node in nodes:
                node.level = level
                # print(node.val, node.level)
                if node.val == target.val:
                    target_level = level
                    # print('here', target_level)
                    break
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            level += 1
            if l:
                q.append(l)

        # print(root.level, target_level)


        res = []




        level = 0
        q = [[target]]
        target_children = []
        while q:
            nodes = q.pop(0)
            l = []
            for node in nodes:
                if level == K:
                    res.append(node.val)
                target_children.append(node.val)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            level += 1
            if l:q.append(l)
        # print(target_children)

        def have_k_distance(node):
            # either found target, must have K distance
            # or not found target
            # print(node.val)
            q = [[node]]
            level = 0
            while q:
                nodes = q.pop(0)
                l = []
                for node in nodes:
                    if node.val == target.val:
                        if level == K:
                        # print(level)
                            return True
                        else:
                            # print(node.val, level)
                            return False
                    if node.left:
                        l.append(node.left)
                    if node.right:
                        l.append(node.right)
                level += 1
                if l:
                    q.append(l)
            return True
        # it's OK to be on the same side
        # distance between node and target must be K
        # target_root_distance = K - target_level
        if target_level <= K:

            q = [[root]]
            level = 0
            while q:
                nodes = q.pop(0)
                l = []
                for node in nodes:
                    if level == K - target_level:
                        if node.val not in target_children and have_k_distance(node): 
                            # print(node.val)
                            res.append(node.val)
                    if node.left:
                        l.append(node.left)
                    if node.right:
                        l.append(node.right)
                level += 1
                if l:
                    q.append(l)
        else:
            q = [[root]]
            level = 0
            while q:
                nodes = q.pop(0)
                l = []
                for node in nodes:
                    if level == target_level - K:
                        # print(node.val)
                        res.append(node.val)
                    if node.left:
                        l.append(node.left)
                    if node.right:
                        l.append(node.right)
                level += 1
                if l:
                    q.append(l)

        # print(res)
        return res

    def distanceK(self, root, target, K):
        # convert tree to graph
        edges = []
        def dfs(node):
            if node:
                if node.left:
                    edge = [node.val, node.left.val]
                    edges.append(edge)
                    dfs(node.left)
                if node.right:
                    edge = [node.val, node.right.val]
                    edges.append(edge)
                    dfs(node.right)
        dfs(root)
        # print(edges)
        if not edges:
            if K == 0:
                return [target.val]
            else:
                return []
        # import networkx as nx

        # g = nx.Graph()
        g = Graph()
        g.add_edges_from(edges)


        def _single_shortest_path(adj, firstlevel, paths, cutoff, join):
            
            level = 0                  # the current level
            nextlevel = firstlevel
            while nextlevel and cutoff > level:
                thislevel = nextlevel
                nextlevel = {}
                for v in thislevel:
                    for w in adj[v]:
                        if w not in paths:
                            paths[w] = join(paths[v], [w])
                            nextlevel[w] = 1
                level += 1
            return paths


        def single_source_shortest_path(G, source, cutoff=None):
            if cutoff is None:
                cutoff = float('inf')
            def join(p1, p2):
                return p1 + p2
            nextlevel = {source: 1}     # list of nodes to check at next level
            paths = {source: [source]}  # paths dictionary  (paths to key from source)
            return dict(_single_shortest_path(G.adj, nextlevel, paths, cutoff, join))
        


        # paths = nx.single_source_shortest_path(g, source=target.val, cutoff=K)
        paths = single_source_shortest_path(g, source=target.val, cutoff=K)
        return [k for k,v in paths.items() if len(v) == K+1]


# s = Solution()

# from tn import buildRoot, null, TreeNode

# root = [3,5,1,6,2,0,8,null,null,7,4]
# target = [5,6,2,null,null,7,4]
# K = 2
# root = buildRoot(root)
# target = buildRoot(target)
# print(s.distanceK(root, target, K))






# root = [0,1,null,3,2]
# target = [2]
# K = 1

# root = buildRoot(root)
# target = buildRoot(target)
# print(s.distanceK(root, target, K)) #[1]



# root = [0,2,1,null,null,3]
# target = [3]
# root = buildRoot(root)
# target = buildRoot(target)
# K = 3
# print(s.distanceK(root, target, K)) #[2]



# root = [0,1,null,null,2,null,3,null,4]
# target = [3,null,4]
# K = 0
# root = buildRoot(root)
# target = buildRoot(target) 
# print(s.distanceK(root, target, K)) #[3]


# root = [0,null,1,2,5,null,3,null,null,null,4]
# target = [2,null,3,null,4]
# K = 2
# root = buildRoot(root)
# target = buildRoot(target) 
# print(s.distanceK(root, target, K)) #[4,5,0]


# root = [1]
# target = [1]
# K = 3
# root = buildRoot(root)
# target = buildRoot(target) 
# print(s.distanceK(root, target, K)) #[]