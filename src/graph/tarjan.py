"""
Algo to find articulation points and bridge
Time: O(m + n)
Space: O(m + n)
"""
from collections import defaultdict


def tarjan_dfs(connections, n):
    low = [0] * n
    num = [0] * n
    ap = [0] * n
    adj = defaultdict(list)
    visited = set()

    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u, par, num_child):
        low[u] = num[u] = num_child
        visited.add(u)

        for v in adj[u]:
            if v == par:
                continue

            if v not in visited:
                num_child += 1
                dfs(v, u, num_child)
                ap[u] |= low[u] >= num[u]
                low[u] = min(low[u], low[v])
            else:
                low[u] = min(low[u], num[v])

        return num_child

    dfs(1, -1, 0)
    # Find bridge
    res = []
    for u in adj:
        for v in adj[u]:
            if num[u] < low[v]:
                res.append([u, v])

    return res


if __name__ == '__main__':
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    res = tarjan_dfs(connections, n)
    print(res)
