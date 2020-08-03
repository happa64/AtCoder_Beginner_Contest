# https://atcoder.jp/contests/arc043/submissions/15663432
# B - 難易度
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class BIT:
    def __init__(self, L):
        self.n = len(L)
        self.bit = [0] * (self.n + 1)

    def update(self, idx, x):
        while idx <= self.n:
            self.bit[idx] += x
            idx += idx & (-idx)

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx] % mod
            idx -= idx & (-idx)
        return res

    def sec_sum(self, left, right):
        return self.query(right) - self.query(left - 1)

    def debug(self):
        print(*[self.sec_sum(i, i) for i in range(1, self.n + 1)])


def resolve():
    n = int(input())
    D = sorted(list(int(input()) for _ in range(n)))
    MAX = max(D)
    L = list(range(MAX))
    dp = [BIT(L) for _ in range(4)]
    for i in range(4):
        for j in range(n):
            d = D[j]
            if i == 0:
                dp[i].update(d, 1)
            else:
                cnt = dp[i - 1].query(d // 2) % mod
                dp[i].update(d, cnt)
    print(dp[-1].query(MAX) % mod)


if __name__ == '__main__':
    resolve()
