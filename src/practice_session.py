def kmp_search_re(haystack, needle):
    pass


if __name__ == '__main__':
    haystack = "aaacdabcbcbc"
    needle = "bc"
    print(kmp_search_re(haystack, needle))
    assert kmp_search_re(haystack, needle) == [6, 8, 10]