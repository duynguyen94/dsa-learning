class Rect:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def contains(self, other):
        return all(self.low[d] <= other.low[d] and self.high[d] >= other.high[d] for d in range(len(self.low)))

    def intersects(self, other):
        return all(self.low[d] <= other.high[d] and self.high[d] >= other.low[d] for d in range(len(self.low)))


class Node:
    def __init__(self, level):
        self.level = level
        self.entries = []

    def is_leaf(self):
        return self.level == 0


class RTree:
    def __init__(self, max_entries=4):
        self.root = Node(1)
        self.max_entries = max_entries

    def insert(self, rect, value):
        leaf = self._choose_leaf(self.root, rect)
        leaf.entries.append((rect, value))
        if len(leaf.entries) > self.max_entries:
            self._split_node(leaf)

    def _choose_leaf(self, node, rect):
        if node.is_leaf():
            return node
        best_child = min(node.entries, key=lambda n: self._enlargement(n[0], rect))
        return self._choose_leaf(best_child[1], rect)

    def _split_node(self, node):
        # Implement node splitting
        pass

    def _enlargement(self, rect1, rect2):
        return Rect(
            [min(rect1.low[d], rect2.low[d]) for d in range(len(rect1.low))],
            [max(rect1.high[d], rect2.high[d]) for d in range(len(rect1.high))]
        ).area() - rect1.area()
