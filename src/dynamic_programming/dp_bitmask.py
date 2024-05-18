"""
Collect from https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
Sample problem: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
Solution from: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/1494961/python-dp-on-subsets-explained
"""


def can_partition_k_subsets(nums, k):
    """
    TC: O(2 ^ n * n)
    SC: O(2 ^ n)
    :param nums:
    :param k:
    :return:
    """
    N = len(nums)
    nums.sort(reverse=True)

    basket, rem = divmod(sum(nums), k)
    if rem or nums[0] > basket:
        return False

    dp = [-1] * (1 << N)
    dp[0] = 0
    for mask in range(1 << N):
        for j in range(N):
            nei = dp[mask ^ (1 << j)]
            if mask & (1 << j) and nei >= 0 and nei + nums[j] <= basket:
                dp[mask] = (nei + nums[j]) % basket
                break

    return dp[-1] == 0


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    assert can_partition_k_subsets(nums, k) is True

    nums = [1, 2, 3, 4]
    k = 3
    assert can_partition_k_subsets(nums, k) is False
