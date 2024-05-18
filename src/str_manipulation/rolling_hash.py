def rolling_hash(haystack, needle):
    base = 256
    mod = 10 ** 9 + 7

    n, m = len(haystack), len(needle)
    hash = [0] * (n + 1)
    # Calculate hash fn
    for i in range(1, n + 1):
        hash[i] = (hash[i - 1] * base + ord(haystack[i - 1])) % mod

    n_hash = 0
    # Calculate hash for needle
    for c in needle:
        n_hash = (n_hash * base + ord(c)) % mod

    powerm = pow(base, m, mod)
    res = []
    # Calculate sub-hash
    for i in range(n - m + 1):
        sub_hash = (hash[i + m] - (hash[i] * powerm) % mod + mod) % mod

        if sub_hash == n_hash:
            res.append(i)

    return res


if __name__ == '__main__':
    haystack = "aaacdabcbcbc"
    needle = "bc"
    print(rolling_hash(haystack, needle))