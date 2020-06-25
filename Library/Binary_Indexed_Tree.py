class BIT:
    def __init__(self, L):
        self.n = len(L)
        self.bit = [0] * (n + 1)

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    def sec_sum(self, left, right):
        return self.query(right) - self.query(left)

    def update(self, idx, x):
        while idx <= self.n:
            self.bit[idx] += x
            idx += idx & (-idx)