def build_z_table(s):
    n = len(s)
    z_table = [0] * n
    match_left = match_right = 0

    for i in range(1, n):
        if i >= match_right:
            match_left = match_right = i

            while match_right < n and s[match_right] == s[match_right - match_left]:
                match_right += 1

            z_table[i] = match_right - match_left
            continue

        if z_table[i - match_left] < match_right - i:
            z_table[i] = z_table[i - match_left]
            continue

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
