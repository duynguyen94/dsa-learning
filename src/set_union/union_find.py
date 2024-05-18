class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, i):
        if i != self.par[i]:
            self.par[i] = self.find(self.par[i])

        return self.par[i]

    def union(self, i1, i2):
        p1 = self.find(i1)
        p2 = self.find(i2)

        if p1 == p2:
            return

        if p1 < p2:
            self.par[p1] = p2
        else:
            self.par[p2] = p1