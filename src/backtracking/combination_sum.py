from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # TC: O(2 ^ n)
    # SC: O(2 ^ n)
    # Practices problem: https://leetcode.com/problems/combination-sum/description/
    if not candidates:
        return []

    res = []
    candidates.sort()

    def dfs(idx, path, cur):
        if cur > target:
            return

        if cur == target:
            res.append(path)
            return

        for i in range(idx, len(candidates)):
            dfs(i, path + [candidates[i]], cur + candidates[i])

    dfs(0, [], 0)
    return res


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    """
    Without any duplication
    TC: O(2 ^ n)
    SC: O(2 ^ n)
    :param candidates:
    :param target:
    :return:
    """
    res = []
    candidates.sort()

    def dfs(idx, path, cur):
        if cur > target: return
        if cur == target:
            res.append(path)
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            dfs(i + 1, path + [candidates[i]], cur + candidates[i])

    dfs(0, [], 0)
    return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(combination_sum(candidates, target))

    candidates = [2, 1, 1, 2, 2, 6, 3]
    target = 6
    print(combination_sum_ii(candidates, target))
