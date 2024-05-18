def coin_change_bot_up(coins, amount):
    # Follow https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
    # TC: O(n * amount)
    # SC: O(amount)

    n = len(coins)
    if n == 0:
        return 0

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(coins[i], amount + 1):
            if dp[j - coins[i]] != float('inf'):
                dp[j] = min(dp[j], 1 + dp[j - coins[i]])

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


def coin_change_top_down(coins, amount):
    n = len(coins)
    if n == 0:
        return 0

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    def dfs(remain):
        if remain == 0:
            return 0

        if remain < 0:
            return -1

        if dp[remain] != float('inf'):
            return dp[remain]

        min_coins = float('inf')
        for coin in coins:
            needed = dfs(remain - coin)

            if needed >= 0 and needed < min_coins:
                min_coins = needed + 1

        dp[remain] = min_coins if min_coins != float('inf') else -1

        return dp[remain]

    return dfs(amount)


if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    assert coin_change_bot_up(coins, amount) == 3
    assert coin_change_top_down(coins, amount) == 3

    coins = [2]
    amount = 3
    assert coin_change_bot_up(coins, amount) == -1
    assert coin_change_top_down(coins, amount) == -1

    coins = [1]
    amount = 0
    assert coin_change_bot_up(coins, amount) == 0
    assert coin_change_top_down(coins, amount) == 0
