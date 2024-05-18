"""
Collect from https://leetcode.com/discuss/general-discussion/662866/DP-for-Beginners-Problems-or-Patterns-or-Sample-Solutions
Sample problem: https://leetcode.com/problems/longest-common-subsequence
"""


def lcs_bottom_up(text1, text2):
    # TC: O(n * m)
    # SC: O(n * m)
    # Follow https://leetcode.com/problems/longest-common-subsequence/solutions/4622129/beats-100-dynamic-programming-c-java-python-js-explained-with-video
    n, m = len(text1), len(text2)

    # Initialize a 2D array (list of lists) with zeros for dynamic programming
    # The array has (len_text1 + 1) rows and (len_text2 + 1) columns
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the characters match, take the diagonal value and add 1
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If the characters do not match, take the maximum of the value from the left and above
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


def lcs_top_down(text1, text2):
    # TC: O(n * m)
    # SC: O(n * m)
    m, n = len(text1), len(text2)
    dp = [[-1] * (n + 1) for _ in range(m + 1)]

    def lcs(i, j):
        if i >= m or j >= n:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = 1 + lcs(i + 1, j + 1)
        else:
            dp[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))

        return dp[i][j]

    return lcs(0, 0)


if __name__ == '__main__':
    text1 = "abc"
    text2 = "abc"
    assert lcs_bottom_up(text1, text2) == 3
    assert lcs_top_down(text1, text2) == 3

    text1 = "abc"
    text2 = "def"
    assert lcs_bottom_up(text1, text2) == 0
    assert lcs_top_down(text1, text2) == 0

    text1 = "abcde"
    text2 = "ace"
    assert lcs_bottom_up(text1, text2) == 3
    assert lcs_top_down(text1, text2) == 3
