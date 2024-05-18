def block_sum_bot_up(mat, k):
    # Follow https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
    # TC: O(m * n)
    # SC: O(m * n)
    m, n = len(mat), len(mat[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

    # calculate prefix sum for matrix
    for i in range(m + 1):
        for j in range(n + 1):
            prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + mat[i - 1][
                j - 1]

    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # +1 because we will use prefix sum matrix
            r1 = max(0, i - k) + 1
            c1 = max(0, j - k) + 1
            r2 = min(m - 1, i + k) + 1
            c2 = min(n - 1, j + k) + 1

            res[i][j] = prefix_sum[r2][c2] - (
                        prefix_sum[r1 - 1][c2] + prefix_sum[r2][c1 - 1] - prefix_sum[r1 - 1][c1 - 1])

    return res


def block_sum_top_down(mat, k):
    # Follow https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
    # TC: O(m * n)
    # SC: O(m * n)
    m, n = len(mat), len(mat[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

    # calculate prefix sum for matrix
    for i in range(m + 1):
        for j in range(n + 1):
            prefix_sum[i][j] = (prefix_sum[i][j - 1]
                                + prefix_sum[i - 1][j]
                                - prefix_sum[i - 1][j - 1]
                                + mat[i - 1][j - 1]
                                )
    dp = dict()

    def dfs(i, j):
        if (i, j) in dp:
            return dp[(i, j)]

        # +1 because we will use prefix sum matrix
        r1 = max(0, i - k) + 1
        c1 = max(0, j - k) + 1
        r2 = min(m - 1, i + k) + 1
        c2 = min(n - 1, j + k) + 1

        block_sum = prefix_sum[r2][c2] - (
                prefix_sum[r1 - 1][c2]
                + prefix_sum[r2][c1 - 1]
                - prefix_sum[r1 - 1][c1 - 1]
        )

        dp[(i, j)] = block_sum

        return dp[(i, j)]

    res = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = dfs(i, j)

    return res


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    assert block_sum_bot_up(mat, k) == [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
    assert block_sum_top_down(mat, k) == [[12, 21, 16], [27, 45, 33], [24, 39, 28]]

    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 2
    assert block_sum_bot_up(mat, k) == [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
    assert block_sum_top_down(mat, k) == [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
