"""
Collect from https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
Sample problem: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
"""
from typing import List


def min_score_triangulation_bot_up(values: List[int]) -> int:
    # follow https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
    # TC: O(n ^ 3)
    # SC: O(n ^ 3)
    n = len(values)

    dp = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):
        i = 0
        while i + l < n:
            j = i + l
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])

            i += 1

    return dp[0][n - 1]


def min_score_triangulation_top_down(values):
    # follow https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/286705/java-c-python-dp
    # TC: O(n ^ 3)
    # SC: O(n ^ 3)
    n = len(values)

    dp = [[float('inf')] * n for _ in range(n)]

    def dfs(i, j):
        if dp[i][j] != float('inf'):
            return dp[i][j]

        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])

        if dp[i][j] == float('inf'):
            dp[i][j] = 0

        return dp[i][j]

    return dfs(0, len(values) - 1)


if __name__ == '__main__':
    values = [1, 2, 3]
    assert min_score_triangulation_bot_up(values) == 6
    assert min_score_triangulation_top_down(values) == 6

    values = [3, 7, 4, 5]
    assert min_score_triangulation_bot_up(values) == 144
    assert min_score_triangulation_top_down(values) == 144

    values = [1, 3, 1, 4, 1, 5]
    assert min_score_triangulation_bot_up(values) == 13
    assert min_score_triangulation_top_down(values) == 13
