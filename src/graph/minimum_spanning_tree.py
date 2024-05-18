# Kruskal and Prim
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Edge:
    def __init__(self, u, weight):
        self.u = u
        self.weight = weight


class SolutionPrim:
    def get_dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim algo
        # TC: O(mlogm), SC: O(m)
        edges = []
        adj = defaultdict(list)
        n = len(points)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = self.get_dist(points[i], points[j])
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        min_dist = [float("inf")] * n
        min_dist[0] = 0
        in_tree = [False] * n

        min_heap = [(0, 0)]
        res = 0

        while min_heap:
            w, u = heappop(min_heap)

            if in_tree[u]:
                continue

            in_tree[u] = True
            res += w

            for (v, dist) in adj[u]:
                if min_dist[v] > dist and not in_tree[v]:
                    min_dist[v] = dist
                    heappush(min_heap, (dist, v))

        return res


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class SolutionKruskal:
    def get_dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def get_root(self, root, x):
        if root[x] == x:
            return x

        root[x] = self.get_root(root, root[x])
        return root[x]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal algo
        # TC: O(mlogm), SC: O(m)
        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append(Edge(i, j, self.get_dist(points[i], points[j])))

        edges.sort(key=lambda x: x.weight)

        n = len(edges)
        root = list(range(n + 1))

        res = 0
        for e in edges:
            u = e.u
            v = e.v
            w = e.weight

            root_u = self.get_root(root, u)
            root_v = self.get_root(root, v)

            if root_u == root_v:
                continue

            root[root_v] = root_u
            res += w

        return res


def get_root(root, x):
    if root[x] != x:
        root[x] = get_root(root, root[x])
    return root[x]


def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def kruskal_algo(points):
    edges = []
    m = len(points)
    for i in range(m):
        for j in range(i + 1, m):
            edges.append([i, j, get_dist(points[i], points[j])])

    edges.sort(key=lambda x: x[2])

    n = len(edges)
    root = list(range(n + 1))

    res = 0
    for e in edges:
        u, v, weight = e
        root_u = get_root(root, u)
        root_v = get_root(root, v)

        if root_u == root_v:
            continue

        root[root_v] = root_u
        res += weight

    return res


def prim_algo(points):
    adj = defaultdict(list)
    n = len(points)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = get_dist(points[i], points[j])
            adj[i].append((j, dist))
            adj[j].append((i, dist))

    n = len(adj)
    min_dist = [float("inf")] * n
    min_dist[0] = 0
    in_tree = [False] * n
    min_heap = [(0, 0)]
    res = 0

    while min_heap:
        w, u = heappop(min_heap)

        if in_tree[u]:
            continue

        in_tree[u] = True
        res += w

        for (v, dist) in adj[u]:
            if min_dist[v] > dist and not in_tree[v]:
                min_dist[v] = dist
                heappush(min_heap, (dist, v))

    return res


if __name__ == '__main__':
    adj = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

    res = prim_algo(adj)
    print(res)