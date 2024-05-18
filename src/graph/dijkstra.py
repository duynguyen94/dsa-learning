from heapq import heappop, heappush


def dijkstra_algo(n, graph, start):
    seen = set()
    dist = [float("inf")] * n
    dist[start] = 0

    min_h = [(0, 0)]

    while min_h:
        cur_dist, u = heappop(min_h)
        seen.add(u)

        for v, w in enumerate(graph[u]):
            new_dist = w + cur_dist
            if dist[v] > new_dist and v not in seen and w != 0:
                dist[v] = new_dist
                heappush(min_h, (new_dist, v))

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
    print(dijkstra_algo(len(graph), graph, 0))