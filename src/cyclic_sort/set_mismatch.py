def set_mismatch_solve(arr: list[int]) -> list[int]:
    """
    Given the list of numbers from 1 to n, we have to find one number that is repeated,
    and another number that is missing from the set.
    We solve this problem by placing the numbers at their correct indexes.
    :param arr:
    :return:
    """
    # Implement cyclic sorting
    start_idx = 0
    print("array", arr)

    while start_idx < len(arr):
        cur_val = arr[start_idx]
        test_idx = cur_val - 1

        if cur_val != arr[test_idx]:
            # Swap
            arr[start_idx] = arr[test_idx]
            arr[test_idx] = cur_val
            print("array", arr)
        else:
            start_idx += 1

    # Double loop => Could we improve it
    for idx, i in enumerate(arr):
        if idx != i - 1:
            return [i, idx + 1]
    return []


if __name__ == '__main__':
    result = set_mismatch_solve([1, 3, 4, 3, 2, 6])
    print(result)
    assert set_mismatch_solve([1, 3, 4, 3, 2, 6]) == [3, 5]
