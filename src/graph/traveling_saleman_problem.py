def tsp(graph, n):
    # TC: O(2 ^ n * n ^ 2)
    # SC: O(2 ^ n * n)

    dp = [[float('inf')] * (1 << (n + 1)) for _ in range(n + 1)]

    def tsp_util(i, mask):
        # base case
        # if only ith bit and 1st bit is set in our mask,
        # it implies we have visited all other nodes already
        if mask == ((1 << i) | 3):
            return graph[1][i]

        if dp[i][mask] != float('inf'):
            return dp[i][mask]

        for j in range(1, n + 1):
            if mask & (1 << j) and j != i and j != 1:
                dp[i][mask] = min(
                    dp[i][mask],
                    graph[i][j] + tsp_util(j, mask & (~(1 << i)))
                )

        return dp[i][mask]

    res = float('inf')
    for x in range(1, n + 1):
        # try to go from node 1 visiting all nodes in between to i
        # then return from i taking the shortest route to 1
        res = min(
            res,
            graph[x][1] + tsp_util(x, (1 << (n + 1))-1)
        )

    return res



if __name__ == '__main__':
    n = 4  # there are four nodes in example graph (graph is 1-based)

    # dist[i][j] represents shortest distance to go from i to j
    # this matrix can be calculated for any given graph using
    # all-pair shortest path algorithms
    dist = [
        [0, 0, 0, 0, 0],
        [0, 0, 10, 15, 20],
        [0, 10, 0, 25, 25],
        [0, 15, 25, 0, 30],
        [0, 20, 25, 30, 0]
    ]

    res = tsp(dist, n)
    print(res)
