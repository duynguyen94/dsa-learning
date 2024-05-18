"""
Sample problem https://leetcode.com/problems/target-sum
"""
from collections import defaultdict


def target_sum_top_down(nums, target):
    # Follow https://leetcode.com/problems/target-sum/solutions/455024/dp-is-easy-5-steps-to-think-through-dp-questions
    # TC: O(n * target)
    # SC: O(n * target)
    n = len(nums)
    cur_sum = 0
    dp = dict()

    def dfs(i, cur_sum):
        if (i, cur_sum) in dp:
            return dp[(i, cur_sum)]

        if i < 0 and cur_sum == target:
            return 1

        if i < 0:
            return 0

        pos = dfs(i - 1, cur_sum + nums[i])
        neg = dfs(i - 1, cur_sum - nums[i])

        dp[(i, cur_sum)] = pos + neg
        return dp[(i, cur_sum)]

    return dfs(n - 1, 0)


def target_sum_bot_up(nums, target):
    # Follow https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
    # TC: O(n * target)
    # SC: O(n * target)
    hm = defaultdict(int)

    # Initialize with sum 0 having 1 way
    hm[0] = 1

    # Iterate over each number in nums
    for num in nums:
        # Create a copy of the current state of hm
        mp = dict(hm)
        # Clear the current state of hm to update it
        hm = defaultdict(int)

        # Iterate over each sum in the copy of hm
        for sum_val, count in mp.items():
            # Update hm for the new sums created by adding and subtracting the current number
            hm[sum_val + num] += count
            hm[sum_val - num] += count

    # Return the number of ways to achieve the target sum S
    return hm[target]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    assert target_sum_top_down(nums, target) == 5
    assert target_sum_bot_up(nums, target) == 5

    nums = [1]
    target = 1
    assert target_sum_top_down(nums, target) == 1
    assert target_sum_bot_up(nums, target) == 1
