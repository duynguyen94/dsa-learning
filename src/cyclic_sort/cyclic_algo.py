def cyclic_sort_algo(arr):
    i = 0
    n = len(arr)

    while i < n:
        correct_idx = arr[i] - 1
        if arr[i] != arr[correct_idx]:
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        else:
            i += 1


if __name__ == '__main__':
    # Applicable only for value in range [1, n]
    # TC: O(n), SC: O(1)
    arr = [3, 2, 4, 5, 1]
    cyclic_sort_algo(arr)
    print(arr)
    assert arr == [1, 2, 3, 4, 5]
