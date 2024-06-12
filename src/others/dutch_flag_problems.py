def pointers_approach(arr):
    # TC: O(n)
    # SC: O(1)
    # Initialisation
    n = len(arr)
    l = 0
    r = n - 1
    i = 0

    while i < n and i <= r:
        # current element is 0
        if arr[i] == 0:
            arr[l], arr[i] = arr[i], arr[l]
            l += 1
            i += 1
        # current element is 2
        elif arr[i] == 2:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        # current element is 1
        else:
            i += 1

    return arr


def counting_approach(arr):
    # TC: O(n)
    # SC: O(1)
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    n = len(arr)

    # Count the number of 0s, 1s and 2s in the array
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1

        elif arr[i] == 1:
            cnt1 += 1

        elif arr[i] == 2:
            cnt2 += 1

    # Update the array
    i = 0

    # Store all the 0s in the beginning
    while (cnt0 > 0):
        arr[i] = 0
        i += 1
        cnt0 -= 1

    # Then all the 1s
    while (cnt1 > 0):
        arr[i] = 1
        i += 1
        cnt1 -= 1

    # Finally all the 2s
    while (cnt2 > 0):
        arr[i] = 2
        i += 1
        cnt2 -= 1

    return arr


if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    assert pointers_approach(arr) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
    assert counting_approach(arr) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
