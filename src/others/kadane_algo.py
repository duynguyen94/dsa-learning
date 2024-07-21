"""
Algo to find the Largest Sum Contiguous Subarray
"""


def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    # The subarray {4,-1, -2, 1, 5} has the largest sum 7.
    assert max_subarray_sum(arr) == 7

    arr = [2]
    assert max_subarray_sum(arr) == 2

    arr = [5, 4, 1, 7, 8]
    # The subarray {5,4,1,7,8} has the largest sum 25.
    assert max_subarray_sum(arr) == 25
