from collections import deque
from typing import List


def is_bipartite(graph: List[List[int]]) -> bool:
    """
    The complexity of the algorithm for checking if a graph is bipartite using BFS can be analyzed in terms of time and space complexity.

    ### Time Complexity
    - **BFS Traversal**: The BFS traversal visits each node and each edge once.
    - **Node Visits**: Each node is enqueued and dequeued exactly once.
    - **Edge Visits**: Each edge is considered twice (once from each endpoint).

    Given:
    - \( V \) is the number of vertices (nodes).
    - \( E \) is the number of edges.

    The time complexity is \( O(V + E) \). This is because:
    - Visiting all nodes takes \( O(V) \).
    - Visiting all edges takes \( O(E) \).

    ### Space Complexity
    - **Color Array**: The `color` array stores the color of each node, which takes \( O(V) \) space.
    - **Queue**: The BFS queue can store up to \( V \) nodes in the worst case, requiring \( O(V) \) space.

    The space complexity is \( O(V) \) due to the storage needed for the `color` array and the BFS queue.

    ### Summary
    - **Time Complexity**: \( O(V + E) \)
    - **Space Complexity**: \( O(V) \)

    This makes the algorithm efficient and suitable for large graphs, where the combination of nodes and edges is manageable within the constraints of the problem.
    """
    # TC: O(V + E)
    # SC: O(V)
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors

    for i in range(n):
        if color[i] == -1:  # If the node is not colored
            queue = deque([i])
            color[i] = 0  # Start coloring with 0

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If the neighbor is not colored
                        color[neighbor] = 1 - color[node]  # Color with opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # If the neighbor has the same color
                        return False

    return True


if __name__ == '__main__':
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    assert is_bipartite(graph) is False

    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert is_bipartite(graph) is True
