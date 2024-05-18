"""
Collect from https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
Sample problem: https://leetcode.com/problems/longest-increasing-subsequence/
"""
from bisect import bisect_left


def lis_bottom_up(nums):
    """
    TC: O(n ^ 2)
    SC: O(n)
    :param nums:
    :return:
    """
    dp = [1] * (len(nums))

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


def lis_top_down(nums):
    """
    https://stackoverflow.com/questions/37561909/does-there-exist-a-top-down-dynamic-programming-solution-for-longest-increasing
    TC: O(n ^ 2)
    SC: O(n)
    :param nums:
    :return:
    """
    dp = [-1] * len(nums)

    def dfs(n):
        if dp[n] != -1:
            return dp[n]

        lis = 1
        for i in range(n):
            if nums[n] > nums[i]:
                lis = max(lis, dfs(i) + 1)

        dp[n] = lis
        return dp[n]

    res = 0
    for i in range(len(nums)):
        res = max(res, dfs(i))
    return res


def list_bsearch_bottom_up(nums):
    """
    TC: O(nlogn), SC: O(n)
    :param nums:
    :return:
    """
    sub = []
    for x in nums:
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)
        else:
            idx = bisect_left(sub, x)
            sub[idx] = x

    return len(sub)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 2, 3]
    assert lis_bottom_up(nums) == 4
    assert lis_top_down(nums) == 4
    assert list_bsearch_bottom_up(nums) == 4

    nums = [7, 7, 7, 7, 7, 7, 7]
    assert lis_bottom_up(nums) == 1
    assert lis_top_down(nums) == 1
    assert list_bsearch_bottom_up(nums) == 1
