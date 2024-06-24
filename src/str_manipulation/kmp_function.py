def build_kmp_table(s):
    n = len(s)
    kmp_table = [0] * n

    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = kmp_table[j - 1]

        if s[i] == s[j]:
            j += 1
            kmp_table[i] = j

    return kmp_table


def kmp_search(haystack, needle):
    kmp_table = build_kmp_table(needle)
    n, m = len(haystack), len(needle)
    result = []
    print(kmp_table)

    j = 0
    for i in range(n):
        while j > 0 and haystack[i] != needle[j]:
            j = kmp_table[j - 1]

        if haystack[i] == needle[j]:
            j += 1
            if j == m:
                # pattern found at i-index
                result.append(i - m + 1)
                j = kmp_table[j - 1]

    return result


if __name__ == '__main__':
    haystack = "aaacdabcbcbc"
    needle = "bc"
    print(kmp_search(haystack, needle))
    assert kmp_search(haystack, needle) == [6, 8, 10]
