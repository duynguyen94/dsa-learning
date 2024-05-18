"""
Collect from https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
Sample problem: https://leetcode.com/problems/palindrome-partitioning-ii
"""


def min_cut_top_down(s: str) -> int:
    # Follow https://leetcode.com/problems/palindrome-partitioning-ii/solutions/1388628/python-simple-top-down-dp-clean-concise
    # Top down
    # TC: O(n ^ 2)
    # SC: O(n ^ 2)
    n = len(s)
    palindome = [[None] * n for _ in range(n)]
    res = [float('inf')] * n

    def is_palindrome(l, r):
        if l >= r:
            return True

        if s[l] != s[r]:
            return False

        if palindome[l][r] is not None:
            return palindome[l][r]

        palindome[l][r] = is_palindrome(l + 1, r - 1)
        return palindome[l][r]

    def dp(i):
        if i == n:
            return 0

        if res[i] != float('inf'):
            return res[i]

        res[i] = float("inf")
        for j in range(i, n):
            if is_palindrome(i, j):
                res[i] = min(res[i], dp(j + 1) + 1)
        return res[i]

    return dp(0) - 1


def min_cut_bot_up(s):
    # Follow https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
    # Bottom up
    # TC: O(n ^ 2)
    # SC: O(n ^ 2)
    n = len(s)
    palin = [[None] * n for _ in range(n)]
    dp = [float('inf')] * n

    for i in range(n):
        palin[i][i] = True

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1

            if l == 2:
                palin[i][j] = s[i] == s[j]
            else:
                palin[i][j] = s[i] == s[j] and palin[i + 1][j - 1]

    for i in range(n):
        if palin[0][i] is True:
            dp[i] = 0
        else:
            for j in range(i):
                if palin[j + 1][i] is True and dp[i] > 1 + dp[j]:
                    dp[i] = 1 + dp[j]

    if dp[n - 1] == float('inf'):
        return 1
    return dp[n - 1]


if __name__ == '__main__':
    s = "aab"
    assert min_cut_top_down(s) == 1
    assert min_cut_bot_up(s) == 1

    s = "a"
    assert min_cut_top_down(s) == 0
    assert min_cut_bot_up(s) == 0

    s = "ab"
    assert min_cut_top_down(s) == 1
    assert min_cut_bot_up(s) == 1

    s = "abbab"
    assert min_cut_top_down(s) == 1
    assert min_cut_bot_up(s) == 1
