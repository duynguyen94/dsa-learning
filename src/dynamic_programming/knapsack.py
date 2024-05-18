import time


def naive_recursive(weights: list, values: list, capacity: int, n: int) -> int:
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] <= capacity:
        return max(
            # Case that including new item into the knapsack
            values[n - 1] + naive_recursive(weights, values, capacity - weights[n - 1], n - 1),

            # Case that excluding current item
            naive_recursive(weights, values, capacity, n - 1)
        )
    else:
        return naive_recursive(weights, values, capacity, n - 1)


def bottom_up_approach(weights: list, values: list, capacity: int, n: int) -> int:
    # Init the table for calculation
    dp = [
        [0 for _ in range(capacity + 1)]
        for _ in range(len(weights) + 1)
    ]

    for i in range(len(weights) + 1):
        for j in range(capacity + 1):

            # Compare with current capacity
            if weights[i - 1] <= j:
                dp[i][j] = max(
                    # Case that including new item
                    values[i - 1] + dp[i - 1][j - weights[i - 1]],
                    # Case that excluding new item
                    dp[i - 1][j]
                )
            else:
                # Move next without adding item
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


def _top_down_dp_traverse(weights: list, values: list, capacity: int, n: int, dp: list[list[int]]) -> int:
    # Base case
    if n == 0 or capacity == 0:
        return 0

    # Retrieve from mem if already solved it  => This is where we optimize the problem
    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if weights[n - 1] <= capacity:
        dp[n][capacity] = max(
            # Case when including new item
            values[n - 1] + _top_down_dp_traverse(weights, values, capacity - weights[n - 1], n - 1, dp),
            # Case when excluding new item
            _top_down_dp_traverse(weights, values, capacity, n - 1, dp)
        )
        return dp[n][capacity]

    # Go next without adding new item
    dp[n][capacity] = _top_down_dp_traverse(weights, values, capacity, n - 1, dp)
    return dp[n][capacity]


def top_down_dp_recursive(weights: list, values: list, capacity: int, n: int) -> int:
    dp = [
        [-1 for _ in range(capacity + 1)]
        for _ in range(len(weights) + 1)
    ]

    return _top_down_dp_traverse(weights, values, capacity, len(weights), dp)


def bottom_up_optimize(weights: list, values: list, capacity: int, n: int) -> int:
    dp = [0 for _ in range(capacity + 1)]

    for i in range(len(weights)):
        # Meaning go backward for capacity
        for j in range(capacity, -1, -1):
            if weights[i] <= j:
                dp[j] = max(values[i] + dp[j - weights[i]], dp[j])

    return dp[capacity]


if __name__ == '__main__':
    capacity_ = 6
    weights_ = [1, 2, 3, 5]
    values_ = [1, 5, 4, 8]

    max_values = 10

    # Approaches
    start = time.time()
    naive_recursive_result = naive_recursive(weights_, values_, capacity_, len(weights_))
    print(f"finish naive_recursive after {round((time.time() - start) * 1000, 7)} msec")
    assert max_values == naive_recursive_result, f"{max_values} != {naive_recursive_result}"

    start = time.time()
    top_down_dp_result = bottom_up_approach(weights_, values_, capacity_, len(weights_))
    print(f"finish bottom_up_approach after {round((time.time() - start) * 1000, 7)} sec")
    assert max_values == top_down_dp_result, f"{max_values} != {top_down_dp_result}"

    start = time.time()
    top_down_dp_result = top_down_dp_recursive(weights_, values_, capacity_, len(weights_))
    print(f"finish top_down_dp_recursive after {round((time.time() - start) * 1000, 7)} sec")
    assert max_values == top_down_dp_result, f"{max_values} != {top_down_dp_result}"

    start = time.time()
    top_down_dp_result = bottom_up_optimize(weights_, values_, capacity_, len(weights_))
    print(f"finish bottom_up_optimize after {round((time.time() - start) * 1000, 7)} sec")
    assert max_values == top_down_dp_result, f"{max_values} != {top_down_dp_result}"
