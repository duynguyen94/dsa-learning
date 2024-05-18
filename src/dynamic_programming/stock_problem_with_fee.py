"""
Sample problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""


def max_profit_bot_up(prices, fee):
    """
    # Follow https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
    # TC: O(n)
    # SC: O(n)
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    n = len(prices)
    if n == 0:
        return 0

    buy = [0] * n
    sell = [0] * n

    buy[0] = -prices[0]
    sell[0] = 0

    for i in range(1, n):
        buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
        sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)

    return sell[n - 1]


def max_profit_top_down(prices, fee):
    """
    # Follow https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/1439821/python-from-top-down-dp-to-bottom-up-dp-o-1-space-easy-to-understand
    # TC: O(N * 2 * 2)
    # SC: O(N * 2)
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    n = len(prices)

    dp = dict()

    def dfs(i, is_buy):
        if i >= n:
            return 0

        if (i, is_buy) in dp:
            return dp[(i, is_buy)]

        res = dfs(i + 1, is_buy)

        if is_buy:
            res = max(res, dfs(i + 1, False) - prices[i])
        else:
            res = max(res, dfs(i + 1, True) + prices[i] - fee)

        dp[(i, is_buy)] = res
        return res

    return dfs(0, True)


def max_profit_bot_up_hiepit(prices, fee):
    """
    # Follow https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/1439821/python-from-top-down-dp-to-bottom-up-dp-o-1-space-easy-to-understand
    # TC: O(N * 2 * 2)
    # SC: O(N * 2)
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    n = len(prices)

    dp = dict()

    def dfs(i, is_buy):
        if i >= n:
            return 0

        if (i, is_buy) in dp:
            return dp[(i, is_buy)]

        res = dfs(i + 1, is_buy)

        if is_buy:
            res = max(res, dfs(i + 1, False) - prices[i])
        else:
            res = max(res, dfs(i + 1, True) + prices[i] - fee)

        dp[(i, is_buy)] = res
        return res

    return dfs(0, True)


def max_profit_bot_up_hiepit(prices, fee):
    """
    # Follow https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/1439821/python-from-top-down-dp-to-bottom-up-dp-o-1-space-easy-to-understand
    # TC: O(N * 2 * 2)
    # SC: O(N * 2)
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(2):
            if j == 1:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][0] - prices[i])
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][1] + prices[i] - fee)

    return dp[0][1]


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    assert max_profit_bot_up(prices, fee) == 8
    assert max_profit_top_down(prices, fee) == 8
    assert max_profit_bot_up_hiepit(prices, fee) == 8

    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    assert max_profit_bot_up(prices, fee) == 6
    assert max_profit_top_down(prices, fee) == 6
    assert max_profit_bot_up_hiepit(prices, fee) == 6
