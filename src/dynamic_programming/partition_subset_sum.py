"""
Collect from https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
Sample problem: https://leetcode.com/problems/longest-increasing-subsequence/
"""


def can_partition_top_down(nums) -> bool:
    """
    TC: O(n)
    SC: O(n)
    :param nums:
    :return:
    """
    total_sum = sum(nums)
    n = len(nums)

    if total_sum % 2 != 0:
        return False

    dp = [[-1] * (total_sum) for _ in range(n)]

    def dfs(i, cur_sum):
        if i > n - 1:
            return False

        if dp[i][cur_sum] != -1:
            return dp[i][cur_sum]

        if cur_sum > total_sum // 2:
            return False

        if cur_sum == total_sum // 2:
            return True

        dp[i][cur_sum] = dfs(i + 1, cur_sum + nums[i]) or dfs(i + 1, cur_sum)

        return dp[i][cur_sum]

    return dfs(0, 0)


def can_partition_bottom_up(nums) -> bool:
    """
    TC: O(n)
    SC: O(n)
    :param nums:
    :return:
    """
    s = sum(nums)

    if s % 2 != 0:
        return False

    dp = [True] + [False] * (s // 2)

    for i in range(len(nums)):
        for c in range(s // 2, nums[i] - 1, -1):
            dp[c] = dp[c] or dp[c - nums[i]]

    return dp[-1]


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    assert can_partition_top_down(nums) is True
    assert can_partition_bottom_up(nums) is True

    nums = [1, 2, 3, 5]
    assert can_partition_top_down(nums) is False
    assert can_partition_bottom_up(nums) is False
