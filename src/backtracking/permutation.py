from typing import List
from collections import Counter


def permute(nums: List[int]) -> List[List[int]]:
    """
    Problem to practice: https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis
    TC: O(n * n!)
    SC: O(n!)
    :param nums:
    :return:
    """
    res = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)

        perms = permute(nums)
        for perm in perms:
            perm.append(n)

        res.extend(perms)
        nums.append(n)

    return res


def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Problem to practice https://leetcode.com/problems/permutations-ii/description/
    TC: O(n * n!)
    SC: O(n!)
    :param nums:
    :return:
    """
    res = []

    def dfs(counter, path):
        if len(path) == len(nums):
            res.append(path)
            return
        for x in counter:
            if counter[x]:
                counter[x] -= 1
                dfs(counter, path + [x])
                counter[x] += 1

    dfs(Counter(nums), [])
    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(permute(nums))
    assert sorted(permute(nums)) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    nums = [1, 1, 2]
    print(permute_unique(nums))
    assert sorted(permute_unique(nums)) == sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]])
