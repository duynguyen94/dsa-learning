"""
Algo to find the shortest path between graph
"""
from collections import deque, defaultdict


def bellman_ford_algo(n, graph, start):
    """
    TC:
    - When the graph connected
        - Best O(E), Average/Worst Case: O(V*E)
    - When the graph is disconnected
        - O(E*(V^2))
    SC: O(V), where V is the number of vertices in the graph.

    - Bellman-Ford algorithm will fail if the graph contains any negative edge cycle.
    :param n:
    :param graph:
    :param start:
    :return:
    """
    dist = [float('inf')] * n
    dist[start] = 0

    # Relax to n-1 time
    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    # Check for negative cycle
    for u, v, w in graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return []

    return dist


if __name__ == '__main__':
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]
             ]
    # Convert graph into the form of u, v, w
    dist_graph = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != 0:
                dist_graph.append((i, j, graph[i][j]))

    # print(bellman_ford_algo(len(graph), dist_graph, 0))
    assert bellman_ford_algo(len(graph), dist_graph, 0) == [0, 4, 12, 19, 21, 11, 9, 8, 14]