def build_z_table(s):
    n = len(s)
    z_table = [0] * n
    match_left = match_right = 0

    # start at 1 because the Z-value for the first character (index 0) is always 0.
    for i in range(1, n):
        # Case 1: i is Outside the Current Matching Segment:
        if i >= match_right:
            match_left = match_right = i

            while match_right < n and s[match_right] == s[match_right - match_left]:
                match_right += 1

            z_table[i] = match_right - match_left

        # Case 2: i is Inside the Current Matching Segment:
        elif z_table[i - match_left] < match_right - i:
            # handles the case where the current position i is within the range of the previously found matching segment
            # [match_left, match_right)
            #
            # if z_table[i - match_left] > match_right - i means that the Z-value extends beyond
            # the current matching segment.
            #
            # If the above condition is true, update z_table[i] with z_table[i - match_left]
            # z_table[i] = z_table[i - match_left]
            # - This means that the Z-value at position i is at least as large as the Z-value at
            # position i - match_left, because the matching prefix extends beyond the current matching segment.
            z_table[i] = z_table[i - match_left]
            continue

        else:
            match_left = i
            while match_right < n and s[match_right] == s[match_right - match_left]:
                match_right += 1
            z_table[i] = match_right - match_left

    return z_table


def z_fn_search(haystack, needle):
    z_table = build_z_table(needle + haystack)
    print(z_table)
    result = []

    for i in range(len(needle), len(z_table)):
        if z_table[i] >= len(needle):
            print(i)
            result.append(i - len(needle))

    return result


if __name__ == '__main__':
    haystack = "aaacdabcbcbc"
    needle = "bc"
    print(z_fn_search(haystack, needle))
    assert z_fn_search(haystack, needle) == [6, 8, 10]
