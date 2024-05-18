import random


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


def partition_k(array, low, high, pivot_idx):
    pivot = array[pivot_idx]

    # Move pivot to the end of arr
    array[pivot_idx], array[high] = array[high], array[pivot_idx]

    # Set pivot_idx to low??
    pivot_idx = low

    for i in range(low, high + 1):
        if array[i] <= pivot:
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            pivot_idx += 1

    array[pivot_idx], array[high] = array[high], array[pivot_idx]
    return pivot_idx


def quick_select(array, low, high, k):
    if low == high:
        return array[low]

    p_index = random.choice(range(low, high))
    p_index = partition_k(array, low, high, p_index)

    if k == p_index:
        return array[p_index]

    elif k < p_index:
        return quick_select(array, low, p_index - 1, k)

    return quick_select(array, p_index, high, k)


def quick_select_ep(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot = arr[random.randint(low, high) % (high - low + 1) + low]
    i = low
    j = high

    while True:
        # This logic define greatest or smallest
        # This is smallest
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    if k - 1 < high - low + 1:
        return quick_select_ep(arr, low, j, k)
    else:
        return quick_select_ep(arr, j + 1, high, k - (low - j + 1))


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [5, 6, 7, 11, 12, 13], f'Error: {arr}'
    print('Test is passed')

    res = quick_select(arr, 0, len(arr) - 1, 2)
    print("top 3 = ", res)
