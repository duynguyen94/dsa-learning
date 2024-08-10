# Inspired https://leetcode.com/problems/data-stream-as-disjoint-intervals/solutions/297728/short-python-union-find-solution

class DynamicDSU(object):
    def __init__(self):
        self.intervals = {}
        self.p = {}

    def exists(self, x):
        return x in self.p

    def add_item(self, x):
        self.p[x] = x
        self.intervals[x] = (x, x)

    def find(self, x):
        if not self.exists(x):
            return None

        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px is None or \
                py is None or \
                px == py:
            return

            # merging, can update to other logic
        self.p[px] = py

        # Other logic
        x_interval = self.intervals.pop(px)

        self.intervals[py] = (
            min(self.intervals[py][0], x_interval[0]),
            max(self.intervals[py][1], x_interval[1])
        )
