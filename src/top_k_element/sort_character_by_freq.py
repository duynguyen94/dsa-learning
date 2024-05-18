import heapq


def sort_k_top(input: str) -> str:
    # Create map with char - freq
    char_freq = {}

    for c in list(input):
        if c not in char_freq:
            char_freq[c] = 0

        char_freq[c] += 1

    # Add to heap
    h = []

    for k, v in char_freq.items():
        heapq.heappush(h, (v, k))

    result = []
    for _ in range(len(h)):
        c, f = heapq.heappop(h)
        result.append(c*f)

    return "".join(result)


if __name__ == '__main__':
    """
    Sort character by frequencies
    """
    assert sort_k_top("buubble") == "bbbuule"
