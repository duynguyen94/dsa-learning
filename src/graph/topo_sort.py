from collections import deque


def topological_sort(adj, n):
    # Calculate in_degree
    in_degree = [0] * n
    for u in range(n):
        for v in adj[u]:
            in_degree[v] += 1

    # Set up starting point, for node with 0 in value
    q = deque()
    for u in range(0, n):
        if in_degree[u] == 0:
            q.append(u)

    num_visit = 0
    while q:
        u = q.popleft()
        num_visit += 1
        print(u, end=" ")

        for v in adj[u]:
            in_degree[v] -= 1

            if in_degree[v] == 0:
                q.append(v)


if __name__ == '__main__':
    # Number of nodes
    V = 4

    # Edges
    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]

    # Graph represented as an adjacency list
    adj = [[] for _ in range(V)]

    for i in edges:
        adj[i[0]].append(i[1])

    print(topological_sort(adj, V))
