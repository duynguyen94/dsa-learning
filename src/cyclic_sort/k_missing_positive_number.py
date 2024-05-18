def k_missing_pos_number(arr: list[int], k: int) -> int:
    """
    Given an array of numbers from 1 to n, we have to find the kth missing number from the list.
    :return:
    """
    # Implement cyclic sort for number less than len(array)
    n = len(arr)
    start_idx = 0

    while start_idx < n:
        cur_val = arr[start_idx]

        # Only care about value less than n
        if cur_val <= n:
            target_idx = cur_val - 1
            if cur_val != arr[target_idx]:
                arr[start_idx] = arr[target_idx]
                arr[target_idx] = cur_val
            else:
                start_idx += 1
        else:
            start_idx += 1

    # Find the kth missing number
    missing_numbers_count = 0
    for idx, i in enumerate(arr):
        if i - 1 != idx:
            missing_numbers_count += 1

        if missing_numbers_count == k:
            return idx + 1

    return 0


if __name__ == '__main__':
    assert k_missing_pos_number([6, 7, 9, 2, 3, 13, 11], 3) == 5
