def floyd_warshall_algo(graph):
    n, m = len(graph), len(graph[0])

    dist = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


if __name__ == '__main__':
    INF = float("inf")
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
    # Function call
    res = floyd_warshall_algo(graph)
    print(res)
