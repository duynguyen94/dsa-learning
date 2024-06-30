"""
Ref problem: https://leetcode.com/problems/partition-to-k-equal-sum-subsets
Sol: https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
Bitmask sol: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/335668/dp-with-bit-masking-solution-best-for-interviews/
"""


def can_partition_k_subsets_dfs(nums, k):
    # TC: O(nlogn)
    # SC: O(n)
    if len(nums) < k:
        return False

    num_sum = sum(nums)
    nums.sort(reverse=True)

    if num_sum % k != 0:
        return False

    n = len(nums)
    subsum = num_sum // k
    target = [0] * k

    def dfs(i):
        if i == n:
            for j in range(k):
                if target[j] != subsum:
                    return False
            return True

        for j in range(k):
            if target[j] + nums[i] <= subsum:
                target[j] += nums[i]
                if dfs(i + 1):
                    return True
                target[j] -= nums[i]

        return False

    return dfs(0)


def can_partition_k_subsets_dp_bitmask(nums, k):
    # TC: 0(N*2^N)
    # SC: 0(2^N)
    if len(nums) < k:
        return False

    num_sum = sum(nums)
    nums.sort(reverse=True)

    if num_sum % k != 0:
        return False

    n = len(nums)
    dp = [False] * (1 << n)
    total = [0] * (1 << n)
    dp[0] = True
    subsum = num_sum // k

    for i in range(1 << n):
        if dp[i] is True:

            for j in range(n):
                # The expression 1 << j shifts the number 1 left by j bits,
                # creating a bitmask where only the j-th bit is set.
                new_subset = i | (1 << j)

                # If they are the same, it means the j-th element was already included in i,
                # and there’s no need to process further.
                if new_subset != i:
                    remaining_capacity = subsum - (total[i] % subsum)

                    # total[i] % subsum gives the current sum of the elements in subset i modulo subsum.
                    if nums[j] <= remaining_capacity:
                        # This condition checks if the current element nums[j] can be added to the current subset
                        # i without exceeding subsum.
                        # means adding nums[j] to subset i forms a valid new subset tmp
                        dp[new_subset] = True
                        total[new_subset] = nums[j] + total[i]
                    else:
                        break

    return dp[(1 << n) - 1]


if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    assert can_partition_k_subsets_dfs(nums, k) is True
    assert can_partition_k_subsets_dp_bitmask(nums, k) is True

    nums = [1, 2, 3, 4]
    k = 3
    assert can_partition_k_subsets_dfs(nums, k) is False
    assert can_partition_k_subsets_dp_bitmask(nums, k) is False
