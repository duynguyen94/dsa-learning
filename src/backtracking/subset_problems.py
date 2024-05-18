from typing import List


def subset(nums):
    """
    Practice problems - https://leetcode.com/problems/subsets/description/
    TC: O(2 ^ n)
    SC: O(2 ^ n)
    :param nums:
    :return:
    """
    res = []
    n = len(nums)

    def backtrack(i, subset):
        res.append(subset)
        for j in range(i, n):
            backtrack(j + 1, subset + [nums[j]])

    backtrack(0, [])
    return res


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """
    Practice problems - https://leetcode.com/problems/subsets-ii/description/
    TC: O(2 ^ n)
    SC: O(2 ^ n)
    :param nums:
    :return:
    """
    res = []
    nums.sort()

    def dfs(idx, path):
        res.append(path)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    res = subset(nums)
    print(res)

    nums = [1, 2, 2]
    print(subsets_with_dup(nums))
