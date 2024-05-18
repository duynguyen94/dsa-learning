def merge_sort(array):
    if len(array) == 1:
        return

    mid = len(array) // 2

    # Divide
    left_arr = array[:mid]
    right_arr = array[mid:]

    # Conquer
    merge_sort(left_arr)
    merge_sort(right_arr)

    # Merge
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            array[k] = left_arr[i]
            i += 1
        else:
            array[k] = right_arr[j]
            j += 1

        k += 1

    while i < len(left_arr):
        array[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        array[k] = right_arr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    assert arr == [5, 6, 7, 11, 12, 13], f'Error: {arr}'
    print('Test is passed')